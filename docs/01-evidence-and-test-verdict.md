# Evidence and test verdict
## Four different tests
1. **Historical case audit, completed:** read the current persisted sales report and copy review. This is a dated record of one owner's campaign, not an independent clinical or causal study and not a fresh Gmail reconciliation.
2. **Competitive and integration desk research, completed:** primary vendor pages show substantial overlap in CRM reporting, AI research, outreach and workflows. The market is not empty.
3. **Offline design checks, completed:** 33/33 synthetic checks pass. They exercise the small reference rules in validation/test_plan.py, not future production code.
4. **Buyer demand, usability, retention and revenue effectiveness, not run:** no interviews, pilot customers, willingness-to-pay experiment, A/B landing test, production security test or live integration load test was conducted.

## Case audit
The current case contains 99 screened candidates,42 initial contacts,9 follow-ups and51 outgoing messages. Nine hard failures and two terminal connection failures are distinct recipients. There is one human decline, zero interested conversations and zero verified cash.

This supports a problem statement around source quality, evidence discipline and lack of qualified conversations. It does not tell us whether price, targeting, copy, timing, sender trust, email-channel fit or the underlying offer caused silence.

A zero-interest campaign cannot establish the application's ability to create revenue. It also cannot establish that nobody wants the product: the campaign sold Toss services, not this proposed application. No product-demand conclusion can be taken from it.

## Observed operational strengths
- Sending had explicit authorisation and limits.
- Known refusals and failed addresses were recorded.
- Follow-up count and initial-send count were separated.
- Delivery-pending and final failure were distinguished.
- Existing prospect tools were sometimes acknowledged rather than labelled missing.
- Report publication was tied to actual deployment confirmation.
- Unrelated campaign messages and old payments were excluded.

These are useful requirements. They are not a complete audit of every action, provider permission or future code path.

## Gaps revealed
- Repeated hourly full-thread reads created quota friction and operating cost.
- A published email and valid MX did not establish an active recipient mailbox.
- Screening volume increased while no buyer-confirmed need emerged.
- Early copy sometimes prescribed large scopes before priority was established.
- Cosmetic web findings could be mistaken for commercially meaningful problems.
- Public reports require deliberate redaction and are snapshots, not live CRM data.
- A single user's authorisation model cannot be inherited by new customers.
- Manual source files are not a multi-user transactional system.

## Offline check groups
V01–V07: verified cash, invoices, screenshots, deposits, duplicate events, refunds, tenant and currency boundaries.
V08–V15: accepted/delivered separation, suppressions, pending/ambiguous sends, opt-outs and follow-up rules.
V16–V22: stale history, revoked connection, unsupported channels, changed draft approval, explicit price and quiet hours.
V23–V30: existing tool, insufficient sample, unsupported causal claims, data gaps, timezone and target arithmetic.
V31–V33: case aggregate reconciliation and target completion.

The implementation is intentionally small and simplified. It omits actual databases, concurrency, OAuth, DSN parsers, language models, browser fetching, KMS, webhook verification and provider dispatch. Future software needs independent tests for all of those. Do not reuse the harness as the production policy engine.

## What changed after testing
- Start with a decision-and-follow-up product for existing demand; treat cold acquisition as a later, separately validated capability.
- Separate provider-verified receipts, owner-reported amounts and invoices.
- Default to drafts/approval; ambiguous sends enter reconciliation instead of automatic retry.
- Refuse to invent probability or diagnoses when data is sparse.
- Meter costly research and human support; do not offer unlimited agents.
- Gate the build on observed customer use and paid renewal.
- Use a modular monolith plus workers instead of a fleet of autonomous agents.

## Verdict
Conditional GO for a low-cost research/pilot phase; NO-GO for a claim of proven revenue outcomes or a public autonomous SaaS launch. This is a positive route to evidence, not a reason to abandon the idea.

