# Multi-user architecture and data plan

## Recommended first architecture
Use a modular monolith: one TypeScript web/API application, PostgreSQL, a durable worker queue, private object storage, a secrets manager and provider adapters. A reliable workflow runner is more useful initially than a fleet of autonomous agents.

Candidate stack: Next.js for web/API, managed PostgreSQL, Supabase Auth/RLS or equivalent controls, and pg-boss or another maintained durable queue. These are recommendations, not installed dependencies. Confirm versions and provider contracts during implementation. Redis is optional; do not add a second datastore without a concrete need.

Two deployable processes are sufficient initially: web/API and worker. Webhook ingress can live in the API and enqueue work.

The public application needs its own provider integration and user OAuth authorisation. Current ChatGPT connector credentials and scheduled automation permissions cannot become the authentication system for other customers.

## Data flow
Browser → authenticated API → workspace-scoped domain services → PostgreSQL.

Provider webhook → signature/authentication validation → durable inbox → normaliser → source events → projections.

Scheduler → local checkpoint jobs → goal and decision services → recommendations → approval/outbox → dispatch worker → provider → reconciliation.

Private reports query authorised projections. Public links use a separate redacted snapshot model.

## Tenant isolation
Every tenant-owned row carries workspace_id. Composite foreign keys such as (workspace_id, opportunity_id) prevent relationships across workspaces.

Use database row-level security plus application authorisation. Apply the boundary to APIs, workers, exports, caches, storage and AI retrieval. Privileged server roles can bypass RLS, so their use needs separate controls and tests.

Workers derive workspace context from trusted connections and authenticated job records. A tenant ID supplied in a request payload is not permission. One person may belong to multiple workspaces with different roles.

Within a workspace, recipient lifetime history spans all campaigns. Across customers, contact history remains private; do not build an exposed shared prospect database.

## Principal entities
| Entity | Important information |
|---|---|
| users, workspaces, memberships | Auth identity, workspace, role, status |
| connections | Provider account, credential reference, scopes, cursor, last success |
| goals, goal_versions | Target, metric basis, currency, deadline, revisions |
| offers, offer_versions | Work, price, exclusions, capacity, approval |
| contacts, businesses, identity_links | Normalised identity, sources, relationship, ambiguity |
| campaigns, contact_campaigns | Purpose and membership; no lifetime-history reset |
| opportunities | Need, authority, budget/readiness, stage, next decision |
| conversations, messages | Provider IDs, direction, classification, private source pointer |
| source_evidence | URL/date, purpose, observation, coverage |
| delivery_events, suppressions | Delay/failure class, restriction, audit history |
| tasks, recommendations | Evidence, owner, due time, state, reason |
| approvals | Exact action version/hash, actor, scope, expiry, policy version |
| action_outbox, dispatch_attempts | Intent key, lease, state, provider ID, reconciliation |
| payment_events, receipts, allocations | Amount, currency, basis, verification, reversal |
| experiments, evaluations | Hypothesis, baseline, segment, result |
| audit_events | Actor, workspace, operation, time, redacted change |
| usage, budgets, subscriptions | Entitlements, metered costs, billing status |
| report_snapshots, share_grants | Allowed fields, audience, expiry, revocation |
| deletion_jobs, retention_policies | Export/deletion progress and purpose-specific retention |

## Uniqueness and accounting constraints
Unique provider message: (provider, connection_id, provider_message_id).
Unique provider event: (provider, connection_id, provider_event_id).
Unique recipient identity: (workspace_id, normalised_address).
Unique action intent: (workspace_id, action_intent_key).
Unique checkpoint: workspace, goal, local date, hour and report version.

Allocate a receipt to eligible goals without double-counting a consolidated cash total. Displaying one transaction in several views is not permission to count it several times.

## Proposed API surface
Create workspace; create/revise goal; get today's actions; list opportunities; accept/reject recommendation; approve/cancel action; connect/revoke provider; receive webhook; preview/confirm import; generate/share/revoke report; inspect usage; export data; request deletion.

All writes require authorised workspace context, validated schemas and audit records. Financial verification cannot be a client-supplied boolean. Material writes need idempotency keys and version checks.

## Hosting on a server
Start with a VPS or container host for TLS/reverse proxy, web and worker, with managed PostgreSQL and object storage where practical. Separate production/staging accounts, databases, secrets and provider environments. The existing static report is not this backend.

Require health checks, migrations, rolling deployments, job leases, redacted logs, alerts, encrypted backups and a tested restore process. Benchmark actual workloads before promising capacity or server cost. Scale workers separately when queue age and database metrics justify it.

Tenant fairness, per-connection quotas and spend limits prevent one customer consuming the platform's full provider/AI budget.

## AI boundary
The model proposes structured classifications, hypotheses and drafts. Deterministic services calculate money, authorise actions and enforce state transitions.

Treat email and web content as untrusted data. Use a tool allowlist, typed outputs, source references, HTML sanitisation, attachment controls and SSRF protection. The model cannot choose arbitrary SQL, private URLs, account identifiers or external actions without server validation.
