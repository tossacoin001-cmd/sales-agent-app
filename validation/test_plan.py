"""Offline plan tests, not SaaS code. Synthetic fixtures; no network or messages."""
import json
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

RESULTS = []
def check(key, name, actual, expected):
    RESULTS.append({'id': key, 'scenario': name, 'passed': actual == expected,
                    'actual': actual, 'expected': expected})

def cash(events, tenant='A', currency='NGN'):
    seen, total = set(), 0
    for e in events:
        if e['tenant'] != tenant or e['currency'] != currency:
            continue
        key = (tenant, e['provider'], e['ref'])
        if key in seen or not e['verified'] or e['kind'] not in ('receipt', 'refund'):
            continue
        seen.add(key)
        total += e['amount'] * (-1 if e['kind'] == 'refund' else 1)
    return total

def event(kind, amount, ref, verified=True, tenant='A', currency='NGN'):
    return dict(kind=kind, amount=amount, ref=ref, verified=verified,
                tenant=tenant, currency=currency, provider='synthetic')

def action(*, status='ready', history_complete=True, connected=True,
           intent='followup', prior_followups=0, hours=48, refused=False,
           local_hour=10, authorised=True, needs_price=False,
           price_present=True, supported_channel=True, draft_changed=False):
    if refused: return 'BLOCK_OPT_OUT'
    if status in ('hard_failure', 'final_timeout'): return 'BLOCK_SUPPRESSED'
    if status in ('pending', 'send_unknown'): return 'HOLD_UNCERTAIN'
    if not connected or not history_complete: return 'HOLD_STALE'
    if not supported_channel: return 'PREPARED_NOT_SENT'
    if not authorised or draft_changed: return 'APPROVAL_REQUIRED'
    if needs_price and not price_present: return 'SCOPE_INCOMPLETE'
    if intent == 'followup' and prior_followups: return 'BLOCK_ALREADY_FOLLOWED'
    if intent == 'followup' and hours < 24: return 'HOLD_NOT_DUE'
    if not 8 <= local_hour < 18: return 'HOLD_QUIET_HOURS'
    return 'ELIGIBLE_FOR_DISPATCH_RECHECK'

def diagnosis(*, sample, replies, tool_exists=False, known_gap=False, synced=True):
    if not synced: return 'RESTORE_DATA_FIRST'
    if tool_exists and not known_gap: return 'CONFIRM_ADDITIONAL_NEED'
    if sample < 30: return 'INSUFFICIENT_EVIDENCE'
    if replies == 0: return 'TEST_TARGETING_OR_RELEVANCE_NO_CAUSAL_CLAIM'
    return 'REVIEW_STAGE_EVIDENCE'

def delivery_state(provider_labels, explicit_receipt=False):
    return 'confirmed_delivered' if explicit_receipt else ('accepted_unknown_delivery' if 'SENT' in provider_labels else 'unknown')

def planning_probability(wins, opportunities):
    # A numerical estimate is withheld rather than borrowing an invented rate.
    return None if opportunities < 30 or wins == 0 else wins / opportunities

def main():
    invoice = event('invoice', 350000, 'invoice')
    screenshot = event('receipt', 350000, 'screenshot', False)
    receipt = event('receipt', 210000, 'deposit')
    check('V01', 'Invoice is not received cash', cash([invoice]), 0)
    check('V02', 'Screenshot or owner claim is not verified cash', cash([screenshot]), 0)
    check('V03', 'Deposit counts only amount actually received', cash([receipt]), 210000)
    check('V04', 'Duplicate payment callback does not double count', cash([receipt, receipt]), 210000)
    check('V05', 'Verified refund reduces net cash', cash([receipt, event('refund', 50000, 'refund')]), 160000)
    check('V06', 'Other workspace receipts excluded', cash([event('receipt', 999999, 'other', tenant='B')]), 0)
    check('V07', 'Currencies never summed without explicit conversion', cash([event('receipt', 100, 'usd', currency='USD')]), 0)
    check('V08', 'Sent without delivery receipt is not delivered', delivery_state(['SENT']), 'accepted_unknown_delivery')
    check('V09', 'Hard failure is suppressed', action(status='hard_failure'), 'BLOCK_SUPPRESSED')
    check('V10', 'Final connection failure is suppressed too', action(status='final_timeout'), 'BLOCK_SUPPRESSED')
    check('V11', 'Pending delivery blocks manual resend', action(status='pending'), 'HOLD_UNCERTAIN')
    check('V12', 'Ambiguous provider timeout blocks blind retry', action(status='send_unknown'), 'HOLD_UNCERTAIN')
    check('V13', 'Opt-out wins over commercial urgency', action(refused=True), 'BLOCK_OPT_OUT')
    check('V14', 'New calendar day never resets lifetime follow-up', action(prior_followups=1), 'BLOCK_ALREADY_FOLLOWED')
    check('V15', 'Less than24h is not eligible', action(hours=23), 'HOLD_NOT_DUE')
    check('V16', 'Partial history fails closed for sending', action(history_complete=False), 'HOLD_STALE')
    check('V17', 'Revoked OAuth pauses writes', action(connected=False), 'HOLD_STALE')
    check('V18', 'Unavailable WhatsApp is prepared only', action(supported_channel=False), 'PREPARED_NOT_SENT')
    check('V19', 'Changed approved draft needs fresh approval', action(draft_changed=True), 'APPROVAL_REQUIRED')
    check('V20', 'No authorisation means no dispatch', action(authorised=False), 'APPROVAL_REQUIRED')
    check('V21', 'Priced scope needs explicit price', action(needs_price=True, price_present=False), 'SCOPE_INCOMPLETE')
    check('V22', 'Quiet hours apply even near a deadline', action(local_hour=23), 'HOLD_QUIET_HOURS')
    check('V23', 'Existing tool is not a proven paid need', diagnosis(sample=40,replies=0,tool_exists=True), 'CONFIRM_ADDITIONAL_NEED')
    check('V24', 'Five-contact copy experiment cannot prove winner', diagnosis(sample=5,replies=1), 'INSUFFICIENT_EVIDENCE')
    check('V25', 'Silence does not prove price objection', diagnosis(sample=42,replies=0), 'TEST_TARGETING_OR_RELEVANCE_NO_CAUSAL_CLAIM')
    check('V26', 'Stale data is a data gap before a sales diagnosis', diagnosis(sample=42,replies=0,synced=False), 'RESTORE_DATA_FIRST')
    check('V27', 'Midnight counters use workspace timezone', datetime.fromisoformat('2026-10-26T23:30:00+00:00').astimezone(ZoneInfo('Africa/Lagos')).date().isoformat(), '2026-10-27')
    check('V28', 'Deposit target mix is720k,not1m', 2*210000+2*150000, 720000)
    check('V29', 'No historical wins means no invented win probability', planning_probability(0,42), None)
    check('V30', 'Unfunded1m goal gap stays visible', max(0,1000000-cash([])), 1000000)
    snapshot = {'screened':99,'initials':42,'followups':9,'outgoing':51,'hard':9,'timeouts':2,'human':1,'interested':0,'cash':0}
    check('V31', 'Reconcile current outgoing to initials+followups', snapshot['initials']+snapshot['followups'], snapshot['outgoing'])
    check('V32', 'Known failures are11 distinct recipients', snapshot['hard']+snapshot['timeouts'], 11)
    check('V33', 'No verified receipts means target not achieved', snapshot['cash']>=1000000, False)
    # Scenario figures are assumptions, not measured SaaS cost or demand.
    scenarios=[('solo_light',15000,3500),('solo_heavy',15000,13500),('team_light',35000,8000),('team_heavy',35000,23000)]
    economics=[{'scenario':n,'price_ngn':p,'assumed_direct_cost_ngn':c,'gross_margin_percent':round((p-c)/p*100,2),'passes_75pct_planning_gate':(p-c)/p>=.75} for n,p,c in scenarios]
    payload={'test_type':'offline specification consistency checks only','production_system_tested':False,'customer_demand_validated':False,'revenue_effectiveness_validated':False,'checks':RESULTS,'passed':sum(x['passed'] for x in RESULTS),'total':len(RESULTS),'aggregate_snapshot':snapshot,'economic_assumptions':economics}
    path=Path(__file__).with_name('results.json');path.write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({'passed':payload['passed'],'total':payload['total'],'result':str(path),'customer_validation':'NOT RUN','production_safety':'NOT TESTED'}))
    if not all(x['passed'] for x in RESULTS):raise SystemExit(1)

if __name__ == '__main__':main()
