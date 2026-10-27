# Reliable execution and integrations

## Before every external write
Require an authorised workspace and connected account, resolved recipient, complete/recent relevant history, allowed purpose, no refusal/failure/pending restriction, a valid window and limit, exact draft approval and current policy. Recheck at dispatch, not just at draft creation.

## Durable sending
1. Persist action intent and domain change in one database transaction.
2. Use a unique workspace intent key and reserve quota atomically.
3. Acquire a worker lease and recheck permission, connection, recipient, draft and new events.
4. Persist dispatching before calling the provider.
5. On acceptance, retain provider ID and accepted status.
6. On a clear rejection, record failure and reconcile quota according to the chosen policy.
7. If submission may have succeeded before a timeout, set send_unknown and hold related sends.
8. Reconcile provider/Sent history using known identifiers and context. Require human review if the result remains ambiguous.
9. A worker restart must not blindly retry an unknown send.

Do not promise exactly-once email delivery. Application idempotency cannot guarantee exactly-once external delivery. The design aims for effectively-once intent handling with conservative reconciliation.

## Incoming events
Validate webhook origin, derive workspace from the trusted connection, persist before acknowledgement, deduplicate and process idempotently. Out-of-order events must not remove an opt-out or terminal failure.

Parse delivery reports using recipient, action and status. A temporary delay is not a hard bounce. A final server timeout is not proof of an invalid address, but still blocks further contact.

Automated notices are not human responses. Unrelated campaigns do not count towards a goal. Low-confidence classification needs review before it changes a high-consequence state.

## Gmail
Use the application's own OAuth integration. Google's current scope documentation classifies gmail.send as sensitive and gmail.readonly/gmail.compose as restricted. Public server-side handling of restricted data has verification and security-assessment implications; validate requirements before promising launch dates.

Use history cursors and push-triggered incremental sync rather than repeatedly reading every thread. Renew watches before expiration; Google documents at least every seven days and recommends daily renewal. An expired history cursor can return 404 and require a full resync.

Handle transient quota errors with bounded backoff, jitter, per-account scheduling and a visible last-success timestamp. Revoked authorisation requires reconnection. Do not translate a quota error into an empty inbox or “no changes.”

Health states: healthy, degraded, stale, revoked and blocked. Show verified coverage. Gmail Sent does not provide open-rate proof or establish recipient delivery.

## Manual and future channels
For an unsupported WhatsApp channel, prepare text and a link. Opening the link is not sending; completion requires a separate confirmation. Do not claim API capabilities the product lacks.

Official WhatsApp integration requires current permission, opt-in, template and service-window rules. The policy identifies a 24-hour customer-service window. Do not use personal-session cookies or informal browser automation for mass outreach.

Microsoft 365 is a later adapter requiring its own permissions, subscriptions, delta-sync and operational review. Similar message formats do not establish equivalent capabilities.

## Payments
Keep SaaS subscription billing separate from each customer's client-receipts ledger. Do not route customer funds through Toss's own merchant account by default.

Verify webhook origin and transaction state. Match provider account, environment, currency, amount and reference. Deduplicate; handle refunds, disputes and reversals.

Paystack documents signature/origin validation and transaction verification. A successful provider payment is distinct from settled bank funds. Use the appropriate goal basis and show both states when needed.

A bank-receipts goal requires account reconciliation. A manually reviewed receipt records reviewer, source and method. Do not promote invoice amounts, transfer screenshots or owner statements to independently verified cash.

Bank destination changes require owner review and verification. The model cannot invent payment instructions.

## Notifications
Meaningful events follow user preferences. Checkpoints are once per workspace-local date/time; no-change hourly checks are silent. A notification retry must not repeat the underlying customer action.

Use IANA timezone rules, including DST and midnight boundaries. Persist UTC event times together with the relevant local rule context.
