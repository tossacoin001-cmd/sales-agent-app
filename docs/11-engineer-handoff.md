# Engineer handoff and intended repository

## Authority
This pack contains planning documents and a synthetic validation harness. It does not contain an application scaffold, production dependencies, live credentials or private customer records.

First inspect the real Visibility OS and TE-OS repositories, assess overlap and propose a reuse map. This planning turn did not audit their current source. Do not copy the canonical sales Site's identity, private logs, mailbox identifiers, incoming messages or bank records into a public repository.

## Intended structure after a build decision
```text
apps/
  web/                 owner UI, authenticated API, webhook ingress
  worker/              sync, jobs, policy rechecks, reconciliation
packages/
  domain/              goals, evidence, opportunities, money, states
  policy/              deterministic permissions and constraints
  connectors/          Gmail, manual, payment adapters
  ai/                  typed prompts, evidence references, evaluations
  db/                  migrations, RLS, synthetic fixtures
  ui/                  accessible shared components
  observability/       redacted logs, metrics, traces
tests/
  unit/
  integration/
  tenant-boundaries/
  concurrency/
  provider-contracts/
  adversarial/
  e2e/
infra/
  containers/
  deploy/
  backup-restore/
docs/
  product/
  decisions/
  runbooks/
```

Share typed contracts. Queue workers do not depend on browser state. Avoid one microservice per “agent.”

## Build backlog
| ID | Work | Depends on | Acceptance |
|---|---|---|---|
| P01 | Audit existing repositories | Build decision | Document reuse/replace boundary |
| P02 | Workspace auth and roles | P01 | Cross-tenant/API/storage/export tests deny access |
| P03 | Goal and money contract | P02 | Minor units, currency, basis, deadline versions |
| P04 | Source events and projections | P02 | Idempotent replay and out-of-order handling |
| P05 | Manual import preview | P03–04 | Confirm purpose and identity before import |
| P06 | Gmail consent and read sync | P04 | Review requirements, cursor recovery, revocation, quotas |
| P07 | Opportunity evidence | P04 | Unknown qualification allowed; notices are not humans |
| P08 | Today's actions | P03, P07 | Three specific cards, source links, stale warning |
| P09 | Drafts and approval | P08 | Exact hash/version, roles, edit invalidation |
| P10 | Outbox and reconciliation | P06, P09 | Concurrency safety; unknown sends held |
| P11 | Suppression and delivery | P04, P10 | Opt-out/final failure win at dispatch |
| P12 | Receipt basis and allocations | P03–04 | No invoice/screenshot cash; refunds and duplicates |
| P13 | Checkpoints | P08 | Local time, DST, deduplication, quiet windows |
| P14 | Usage and billing | P04 | Signed events, correct entitlements and spend pauses |
| P15 | Report separation | P02, P04 | Public allowlist; no reply/bank leakage |
| P16 | Export/deletion/retention | P02, P04 | Permissioned export and documented retention |
| P17 | Operations and restore | All critical | Restore exercise, alerts, rollback, incident owner |
| P18 | Invited paid beta | All critical | Evidence gate and capacity approved |

## Mandatory production tests
- Two workers claim the same intent: only one advances.
- Provider accepts, then request times out: reconcile without blind retry.
- Opt-out arrives between approval and dispatch: block.
- Previous campaign decline prevents a new campaign reset.
- Revocation stops queued writes.
- Quota failure shows stale coverage, not a fabricated empty inbox.
- History cursor expires: resync without duplicate records.
- Duplicate/out-of-order webhooks preserve state.
- Recipient or price changes after approval require approval again.
- Workspace switching cannot leak cached context.
- Malicious email instructions do not override policy.
- Source URL to an internal network is blocked.
- Invoice, deposit, refund, dispute and settlement remain distinct.
- One receipt in multiple views does not inflate cash.
- Currency exponent, midnight and DST boundaries calculate correctly.
- Checkpoint retries do not duplicate notices.
- Public report payload excludes private fields entirely.
- Deletion/disconnect and backup retention match documentation.
- Billing retries do not charge or activate the wrong account.
- Backup restore does not replay external actions unsafely.

These tests have not been executed against production code.

## Definition of done
Acceptance behaviour, material failure tests, reviewed provider contracts, redacted secrets, tenant-boundary checks, audited cash calculations, observable jobs, honest UI limitations and rollback instructions.

Use owned test accounts and approved provider sandboxes. Never test email software on unqualified real prospects. A later build instruction—not this document—sets implementation authorisation.
