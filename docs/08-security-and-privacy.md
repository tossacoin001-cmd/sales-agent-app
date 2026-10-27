# Security and privacy requirements

## Trust boundary
The current owner's permission does not authorise another person's mailbox, contacts or campaigns. Each workspace owns its connections, offers, approvals, budgets and reports. New accounts start in read/draft mode.

## Isolation tests before beta
User A cannot retrieve workspace B's opportunity, attachment, search result, export, report or model context. Test the same user switching between workspaces. Reject worker jobs whose connection and workspace do not match. Cache keys and vector searches carry the tenant boundary.

Storage paths and signed download links require object-level authorisation. Support access must be time-limited, consented and audited. Privileged database roles cannot silently bypass isolation.

These tests have not run against a real application. They are launch blockers; the offline harness is not a substitute.

## Secrets and untrusted content
Encrypt OAuth refresh tokens with managed keys; prefer secret references. Rotate/revoke without leaking tokens into logs. Use TLS, access-controlled object storage and redacted telemetry.

Do not place raw email bodies in analytics or exception traces. Sanitise HTML, constrain attachment processing and block private-network/SSRF fetches. Email content cannot instruct an agent to override policy.

## Consent and purpose
Explain what data is read, why, how long it remains, which subprocessors/AI providers receive it, what the app may send and how to revoke access.

Separate read access from outbound permission. Owner approval cannot override channel terms or recipient rights. Review Google Limited Use and Workspace policies against actual vendor/data paths. Shared model training on private mail is off by default.

Provide export, disconnect, deletion and retention controls. Explain backup erasure windows and source-provider limitations.

For a pilot, a possible starting proposal is raw bodies for 30 days only where essential and event metadata for 90 days. These are proposed settings, not legal requirements. Financial records, audit evidence and suppressions need their own retention analysis.

## Suppressions
Opt-outs and final failures persist across a workspace's campaigns and dates. Never expose refusal identities or reasons publicly.

A platform abuse-prevention mechanism may need minimal restricted metadata, but must not reveal one customer's relationships to another. Deletion versus ongoing suppression requires documented legal/policy handling; do not silently reactivate opted-out contacts.

## Sharing
Reports are private by default. Public sharing requires explicit selection, preview, field allowlists, revocation and suitable expiry.

Use a separate redacted read model. Hiding fields with CSS is not privacy. Exclude incoming text, bank details, credentials, private notes and unapproved case-study identities. Evidence links obey permissions too.

## Jurisdiction and provider review
Map customer/recipient locations and processing regions. Assess applicable duties for lawful basis, controller/processor roles, contracts, transfers, rights and registration. Consult qualified privacy expertise for the actual implementation.

The NDPC Act/guidance and provider policies are research inputs. This document does not establish global legal compliance. Gmail verification/security assessment and WhatsApp permission may materially affect budget and timeline.

## Operations
Least privilege, owner/admin MFA, session revocation, audited role changes, rate limits and abuse detection are required.

Incident response: pause writes, contain access, identify affected workspaces, preserve redacted evidence, communicate under applicable requirements, fix and verify before resuming.

Backups are not proven until restored. Schedule access, dependency, restore and incident reviews throughout operation.
