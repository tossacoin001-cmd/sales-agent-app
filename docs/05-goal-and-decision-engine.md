# Goal, evidence and decision engine

## Metric contract
A goal has: id, workspace_id, type, currency, target, start_at, deadline_at, timezone, baseline, inclusion_policy, owner_id and version.

For money, store integer minor units. Do not use binary floating-point for ledger arithmetic. Currency exponent belongs to the currency definition. NGN and USD goals cannot be silently summed.

Cash progress = verified eligible receipts − verified eligible refunds and reversals, using the goal's stated basis.

Customer payment success, provider available balance and bank settlement are different states. A bank-receipts goal counts settled and reconciled account funds; a successful checkout alone is insufficient. Captured payments can be shown separately.

Gross/net basis, fees, taxes, old receivables and deposits must be explicit. Revenue is not profit. Owner-entered amounts stay owner-reported until verified under the agreed policy. A revised goal must keep its prior version and audit record.

Gap = max(0, target − verified progress). Show overachievement separately. A deadline remains overdue until the owner changes it; never silently move the deadline or lower the target.

## Feasibility without invented certainty
Two full ₦350k projects plus two ₦150k projects equal ₦1m in contract value. If the larger projects pay 60% deposits and the smaller projects pay in full, immediate receipts are only ₦720k.

The remaining ₦280k should stay visible. Offer scenarios using actual approved prices, delivery capacity, available hours and payment terms. Do not invent buyers or close probabilities to make the target look attainable.

When zero qualified opportunities exist, explain that the current pipeline cannot support a reliable cash forecast. Recommend a relevant research or owner-conversation task. Emails sent are not a revenue forecast.

An illustrative scenario can use owner-supplied rates, labelled assumptions. Historical estimates later need cohort definitions, time windows and uncertainty. A proposed minimum of 30 comparable observations is only a display safeguard; it does not establish statistical validity.

## Evidence ladder
- Source-backed: an actual provider event, official website fact or verified financial record.
- Owner-confirmed: a statement about a need, decision or offline action, with its source.
- Inferred: a hypothesis from events, labelled as such.
- Unknown: insufficient reliable evidence.
- Contradicted: conflicting evidence that needs review.

Each recommendation stores evidence references, timestamps, coverage and what would change the recommendation. A confidence percentage without an explanation is insufficient.

## Independent state machines
| Domain | Representative states |
|---|---|
| Contact permission | unknown, permitted, restricted, opted_out |
| Message | draft, approved, queued, dispatching, accepted, send_unknown, failed |
| Delivery | unknown, pending, confirmed_delivered, hard_failure, final_connection_failure |
| Conversation | no_human_response, question, interested, objection, declined, uncertain |
| Deal | unqualified, qualified, scoping, scope_agreed, payment_due, won, lost |
| Payment | reported, provider_success, settled, verified_reconciled, refunded, disputed, reversed |

An accepted send does not establish delivery. Delivery does not establish interest. Interest does not establish budget or authority. A written scope is not a receipt.

## Priority algorithm, version 0
Apply permission, policy and financial gates before ranking actions. Then prioritise:

1. A real customer request or decision due soon.
2. A qualified opportunity blocked on a specific owner action.
3. An agreed follow-up or scope decision with clear context.
4. A data correction that unlocks valid work.
5. New research with plausible fit and a verified source.

Use due time, relevance, effort, relationship and evidence freshness. Show the ranking reason. Begin with explainable rules; there is no justified dataset for a black-box revenue score yet. Show at most three priority cards while retaining an inspectable full queue.

## Diagnose the right gap
Data gap: a disconnected source, partial history or unmatched payment.
Activity gap: an agreed action lacks completion evidence.
Delivery gap: pending or failed mail; more sending does not resolve it.
Conversation gap: little human response; targeting, channel, trust and relevance remain alternative explanations.
Qualification gap: interest without need, approver, budget or readiness.
Scope gap: interested buyer without concrete work, price and terms.
Decision gap: a scope exists but no written decision.
Collection gap: accepted work or invoice without verified funds.
Capacity gap: the goal exceeds practical delivery capacity.

The engine should not prescribe more prospecting for every problem.

## Experiment ledger
Store hypothesis, observed fact, alternatives, segment, one change, baseline/control, dates, owner, time/cost budget, metric, stop rule and result. Include adverse outcomes and nonresponders. A five-message price-placement sample is exploratory and cannot establish a winning variant.

Tenant preferences may retain approved offers and playbooks. Private customer messages must not flow into shared model training or another tenant's context by default. A tactic that worked in one small cohort is not automatically a universal recommendation.
