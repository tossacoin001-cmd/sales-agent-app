# Product specification — first sellable experience
## Scope
First release:one workspace, one primary business pipeline, one native currency per goal, email or approved manual records, owner plus a small team. Multiple users in isolated workspaces are mandatory from the first SaaS deployment. Multiple countries are supported by data design, not a promise that every channel, payment method and law is supported at launch.

## Onboarding
1. Select workspace name, country, timezone, currency and role. Explain what connecting data allows.
2. Choose an objective:verified cash, signed scope, qualified conversation or confirmed appointment.
3. Enter target, start date, deadline andbaseline. Define inclusions:deposits/refunds/taxes/old receivables; store the exact basis.
4. Describe offer, price range, delivery capacity, ideal customer and existing tools. Do not auto-install replacement tools.
5. Connect the selected business source through owned OAuth or supply an explicit structured record. Preview scope; limit imported messages by agreed purpose.
6. Set contact/send windows, permissions, daily ceilings and approval mode. New tenant starts read-only/draft-only.
7. Review the first evidence summary and choose the first action. No fake progress animation or invented recovered money.

Acceptance:owner can explain their goal's evidence definition; unknown data is labelled; no external write occurs during signup.

## Primary screen:Today
Above the fold:
- Target, deadline, verified progress, gap and last evidence timestamp.
- Connector health and data coverage, not a misleading green “all good.”
- Up to3specific action cards; show business/person context privately, why now, source record, expected type of benefit, confidence basis, effort andowner.
- One button per next decision:review reply, approve draft, confirm scope, log outcome or resolve data issue.
- Quiet empty state when nothing meaningful changed.

Example action: “Review the quote decision due today. The buyer asked for delivery timing; no reply recorded since yesterday.” This is supported by a thread. “Send50emails to hit your goal” is not an evidence-based recommendation.

## Goal board
Show verified cash, reported cash, invoiced value and pipeline value separately. Let owner revise goal/deadline with an audit trail; never silently lower a target or call it achieved. Show actual progress over time, not only a percentage.
A feasibility panel uses offer economics, capacity, remaining time andexplicit assumptions. If historical conversion data is absent, show scenario arithmetic and “insufficient history” rather than a win probability.

## Pipeline and conversation view
Contact/business identity; source; relationship; existing tools; actual need; location; approver; budget/readiness; quoted scope; next decision; responsible person; last relevant event; contact permission; delivery state.
Qualification fields can be unknown. A single positive sentence does not auto-fill budget or authority.
Thread links and evidence are private. Staff can see only permitted workspaces and assigned records as defined by roles.
A conversation can be interested, declined, question, objection, automated notice, delay, bounce oruncertain. Low-confidence/high-consequence classifications require review.

## Action states
Suggested → reviewed → approved → queued → dispatching → accepted → reconciled.
Alternative states:edited, blocked, stale, revoked, send_unknown, failed, cancelled.
Suggested is not approved; approved is not executed; accepted is not delivered; customer response is not cash.
An approved draft changing its recipient, body, scope, price orpolicy context invalidates approval.
A new opt-out orfailed delivery between approval anddispatch blocks the queued action.

## Opportunity decisions
Prepare one concise qualification reply based on what is missing; do not re-ask known answers.
Recommend one offer only after evidence supports it. Show exact inclusions, exclusions, price, timeline, revision allowance anddecision request.
Contracts, discounts, payment destination changes andother financial commitments require explicit owner approval.
Track a written acceptance separately from signed contract status, payment due andverified receipt.

## Loop diagnosis
Present:
1. Observed fact and source/date.
2. Missing or weak evidence.
3. Plausible explanations labelled hypotheses.
4. One bounded experiment with owner andtime budget.
5. Review date and success/stop rule.
Do not claim “your customers think prices are high” from no replies. A request for clarification can support “scope may be unclear,”but causality remains tentative.

## Accountability
Owner chooses cadence andquiet hours. Checkpoint report compares planned versusactual andasks forone decision when necessary. Notifications deduplicate byevent/goal/checkpoint ID.
If a task is unconfirmed, report it as overdue/unverified. The product cannot mark it done to keep a streak.
Use reminders that reduce effort; avoid shame, panic, fictional urgency andpressure around financial distress.

## Mobile experience
Responsive web/PWA first. Comfortable touch targets, short cards, editable draft preview, low-data pages andoffline reading of a clearly stale cached snapshot. External sends require a live authorised server-side recheck. Native mobile applications are later, only after demand.

## Permissions
Owner:policies, billing, exports, connections, commercial approvals.
Manager:pipeline/team actions within permission, approve routine messages if delegated.
Member:assigned tasks, notes, drafts; no unrestricted policy orbank changes.
Viewer/finance:explicit read access; finance verification requires a separate permission.
Support:time-limited, consented access with an audit trail; no default all-tenant browsing.

## MVP exclusion list
No autonomous cold lead scraping, no informal WhatsApp session automation, no ad purchasing, no custom app builder, no lender/no guaranteed income, no automatic contract acceptance, no universal bank aggregation, no broad multi-currency consolidation, no public client inbox.

