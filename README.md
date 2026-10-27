# Toss Revenue Execution — product and repository blueprint
Version 0.1 • Prepared 27 October 2026 UTC; source case reconciled 26 October 2026 Lagos.
Working product name only. No naming clearance or availability claim.

## Decision
**Proceed to customer discovery and a small paid concierge pilot. Do not build or publicly launch the SaaS yet.**

The existing agent demonstrates a useful supervised workflow: source checking, personalised drafts, permanent suppressions, once-only follow-ups, dated evidence and accountability. It does not yet demonstrate repeatable customer acquisition or new revenue. A multi-user application is a new product with additional security, integration, operating-cost and support requirements.

This is a documentation repository plus an offline validation harness. It is not a working application, production architecture implementation, tested sending service or published GitHub repository. No application was built, deployed or sold during preparation. No new prospects were contacted. Existing automations and the sales dashboard were not changed for this product-planning task.

## Product thesis
**An owner sets a cash or sales goal and a deadline. The product connects permitted evidence, shows the gap, and presents the few next actions worth taking—with an explanation and a clear approval boundary.**

Customer wording to test:
> Know where your sales goal stands—and what to do next.

Supporting sentence:
> Bring your enquiries, follow-ups and payment records into one daily plan. See what is confirmed, what needs attention and which action is yours to approve.

This is a hypothesis about a useful product, not a conversion guarantee. Revenue execution is the first module; do not expand into a general life coach, finance lender, ad buyer, website builder and CRM replacement.

## Start with one buyer
An owner-led service business or small agency with existing enquiries/quotes, repeat follow-up work and a digital record they can authorise us to use. Start with project-based agencies and service providers reachable through email. Test local event, photography or commercial-service businesses as a separate cohort when their records are accessible.

Avoid the first release for: businesses with no viable offer, emergency-cash expectations, no permission to access records, no usable digital history, a need for bulk unsolicited WhatsApp, regulated high-stakes advice, or complex multinational enterprise requirements.

Global ambition is supported by tenant isolation, local timezones, currencies and channel capabilities. Global go-to-market comes after a narrow paid cohort works.

## Evidence, not enthusiasm
Latest available case snapshot—not a fresh inbox check in this planning turn:
- 99 candidates screened; 42 distinct businesses initially emailed.
- 9 lifetime unsolicited follow-ups; 51 outgoing campaign messages.
- 9 hard bounces, 2 final server-connection failures, 0 pending deliveries.
- 1 human reply, a decline; 0 interested conversations, qualified needs, scopes or verified new receipts.
- ₦0 account-verified new cash at the 26 October evening close.
- Hard-bounce share of initial-contact attempts: 9/42 = 21.43%.
- Known failed-recipient share, including final connection timeouts: 11/42 = 26.19%.
- These are descriptive attempt-level ratios. Remaining recipients are not verified delivered.
- Automation logs demonstrate some rule handling. They do not prove that all untested cases or production safety requirements are satisfied.

The agent has helped establish process discipline. “Working perfectly” is not yet a defensible product or sales claim.

## What is inside
| File | Purpose |
|---|---|
| docs/01-evidence-and-test-verdict.md | What was actually tested and what remains unproven |
| docs/02-buyer-and-value.md | Buyer selection, valuable workflows and differentiation |
| docs/03-validation-before-build.md | Interview, pilot, willingness-to-pay and stop/go gates |
| docs/04-product-specification.md | Onboarding, screens, goals, decisions and acceptance criteria |
| docs/05-goal-and-decision-engine.md | Evidence states, arithmetic, diagnosis and learning |
| docs/06-architecture-and-data.md | Multi-tenant deployment, entities and interfaces |
| docs/07-execution-and-integrations.md | Reliable jobs, Gmail, manual channels and payments |
| docs/08-security-and-privacy.md | Tenant isolation, roles, secrets, consent and sharing |
| docs/09-pricing-and-economics.md | Test prices, direct cost scenarios and spend limits |
| docs/10-roadmap-and-launch.md | Stage gates, work packages and launch experiment |
| docs/11-engineer-handoff.md | Repository layout, issue backlog and definition of done |
| docs/12-risk-register.md | Failure modes, ownership and stop conditions |
| docs/13-source-register.md | Primary research, exact URLs and limitations |
| docs/14-policy-and-migration.md | Per-customer permissions and safe reuse of existing work |
| examples/owner-day.md | Fictional owner experience showing concrete value |
| examples/pilot-scorecard.csv | Blank measurement sheet; no invented participants |
| validation/test_plan.py | Offline design-rule harness; no network or messages |
| validation/results.json | Actual harness output |
| validation/business-validation-register.csv | Untested business assumptions and validation status |

## Run the only executable component
Use Python 3.9+ with zoneinfo support:
```bash
python validation/test_plan.py
```
It runs synthetic specification checks, writes validation/results.json, and does not access email, payments, real people or external services. Passing is not a claim of real queue safety, OAuth compliance, database isolation or sales effectiveness.

## Launch gate
Do not call this a proven growth product until real customers repeatedly use it, pay/renew, and a documented pilot shows a useful measurable result. Before any public multi-user launch: integration approval requirements, tenant-boundary tests, ambiguous-send handling, restore drill, billing tests and privacy review must pass.

## Relationship to Toss Enterprise
Build on Toss Visibility OS or TE-OS only after inspecting the real repositories and confirming overlap. Their current source was not audited in this task. Prefer a shared account/workspace foundation and a separately metered Revenue Execution module over another disconnected product. Keep agency services and SaaS subscriptions commercially separate. The approved ₦50k/₦150k/₦350k client services do not automatically become this application's subscription plans.

Next authorised planning step: owner reviews this pack; then recruit discovery participants with explicit research permission. Do not interpret this document as permission to build, charge customers, send research invitations or deploy.

