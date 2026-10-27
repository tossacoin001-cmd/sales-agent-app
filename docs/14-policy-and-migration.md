# Policy configuration and migration

## Customer policy is a first-class object
Each workspace has a versioned policy: enabled channels, authorised purposes, quiet hours, daily budgets, contact cadence, approval roles, price/scope rules and public-sharing settings.

The present Toss campaign's 15-new/5-follow-up daily ceilings are its owner's authorisation, not a universal SaaS entitlement. Do not silently grant those permissions to every customer. A new workspace begins in read/draft mode; any external execution needs explicit setup and server-enforced platform limits.

The offline harness uses the current campaign's conservative once-only follow-up rule. A future consented customer workflow may have a different approved cadence. Define it in a versioned policy, test it and disclose it; never remove an opt-out or known failure to satisfy a cadence. No new date or campaign resets contact history.

## What can be reused from the existing experiment
Concepts: evidence ledger, source checks, count definitions, suppression handling, concise drafts, checkpoints, privacy exclusions and verified publication records.

What must be rebuilt or formally audited: transactional storage, tenant isolation, account permissions, job concurrency, provider integration, approval records, billing and financial reconciliation.

Do not migrate the current owner's whole mailbox or private activity directory into a shared SaaS database as seed data. Use synthetic fixtures. For a later authorised migration, preview selected business records, resolve duplicates, carry suppressions and lifetime history, preserve source timestamps and require an explicit import decision.

## Existing product audit checklist
Inspect actual auth, user/workspace model, hosting, database, permissions, API routes, billing, connectors, task logic and event history in Visibility OS and TE-OS.

Produce a table: component, current evidence, reusable unchanged, reusable with changes, replace, unknown. Decide whether Revenue Execution is a paid OS module or a separate product with shared identity. Do not duplicate accounts or subscriptions without a customer reason.

## Migration acceptance
Counts reconcile to source; no lost suppressions; imported claims retain their evidence status; old payments do not become new-client receipts; users see only their authorised records; rollback is available before any external write is enabled.
