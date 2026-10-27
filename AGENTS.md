# Instructions for future coding agents

This is a planning repository. Do not start a production app, deploy, send messages, incur costs or charge customers unless separately instructed.

1. Read README.md and docs/01-evidence-and-test-verdict.md first.
2. Inspect validation/business-validation-register.csv. Offline tests do not validate demand or production safety.
3. Preserve the difference between facts, hypotheses and unknowns.
4. Keep money in integer minor units, with currency and an explicit goal basis. Invoices and screenshots are not verified receipts.
5. Do not copy customer data or the canonical sales Site's private files into this repository.
6. New customers need their own connections, permissions, policies and isolated workspaces. The owner's current automation authorisation does not transfer to them.
7. External actions need deterministic server-side gates, approval/version binding and conservative handling of ambiguous sends.
8. Inspect actual Visibility OS/TE-OS source before proposing reuse. Do not claim those repositories were audited here.
9. Recheck current provider documentation before implementing APIs, OAuth scopes, billing or deployment dependencies.
10. Prioritise a working owner decision loop over feature count, agent count or send volume.
