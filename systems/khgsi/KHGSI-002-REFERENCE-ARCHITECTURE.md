# KHGSI-002 — Reference Architecture and System Boundaries

**Status:** Architecture specification; integrations NOT VERIFIED.  
**Design rule:** One unified ecosystem; multiple independent systems; shared infrastructure; external human authority.

## 1. Logical architecture

```text
                  EXTERNAL HUMAN AUTHORITY
                             |
                    Human decisions / receipts
                             |
              +--------------v--------------+
              | Primordial Rule + Constitution|
              | independently enforced       |
              +--------------+--------------+
                             |
                    Federation Governance
                             |
       +---------------------+---------------------+
       |                     |                     |
  Central Controller   Cyber Defense Plane   Evidence / Ledger
       |                     |                     |
       +---------- KCN Link Bridge ---------------+
                             |
                 Permission-aware interfaces
                             |
  +--------------------------+---------------------------+
  |                          |                           |
Data Layer             Intelligence Engines         Assurance
  |                    |                             |
  |              +-----+--------------------+        |
  |              |                          |        |
  |          Builder / URSIE             Solver      |
  |              |                          |        |
  |        Representation Core        Research &    |
  |                                   Computation   |
  |                                                  |
  +----------------------+---------------------------+
                         |
                MANIFEX / Engineering
                         |
                  AHM repair workflow
                         |
                 Preflight verification

        Isolated Scientific Research Laboratory
        (controlled inputs/outputs; no direct production write)

Cybersecurity spans every component, connection, artifact store, and runtime.
```

The diagram expresses intended boundaries. It is not evidence that these connections exist in code.

## 2. Responsibility separation

| Component | Responsibility | Must not become |
|---|---|---|
| External Human Authority | Human direction, required authorization, ratification | Software role or service account |
| Primordial Rule | Non-overridable foundational restriction | Runtime-editable policy |
| Constitution | Governing constraints and amendment process | Self-modifying agent instructions |
| Federation | Membership, trust, scoped permissions, revocation | Collective sovereignty |
| Data Layer | Shared authorized artifacts, provenance, lineage | Unrestricted shared filesystem |
| KCN Link Bridge | Authenticated, authorized interoperation | Permission escalation path |
| Central Controller | Planning and workflow coordination | Authority issuer or sole enforcement point |
| Builder / URSIE | Representation, interpretation, translation, reconstruction | Governance authority |
| Universal Solver | Candidate reasoning and solutions | Implementation approver |
| Preflight | Inspection, testing, verification evidence | Self-ratifying authority |
| AHM | Investigation and in-scope healing | Unrestricted production administrator |
| Research Laboratory | Isolated research and experiments | Production deployment authority |
| Cyber Defense Plane | Detection, containment, evidence, recovery coordination | Exempt or unchecked authority |
| MANIFEX / engineering | Engineering lifecycle within scope | Unrestricted system-wide control |

## 3. Eleven intelligence families

The registry groups linguistic, mathematical, symbolic, computational, physical, quantum, information, anomaly, algorithmic, scientific-discovery, and cybersecurity/defensive intelligence. Each family may contain multiple independent engines. A family label is not a runnable tool.

## 4. Core interfaces

These are target contracts, not assertions that an implementation already exists.

### Capability descriptor

Each record must provide stable capability and system IDs; responsibility; version; entry point or transport; input/output schemas; permissions and risk class; dependencies; security requirements; evidence and verification status; limitations; source repository/path and artifact digest; and health/availability with measurement timestamp.

### Invocation envelope

A future Bridge invocation carries request and correlation IDs, requesting identity, target system/capability, input artifact IDs/digests, declared purpose and scope, policy version and authorization reference where required, deadline/resource budget, idempotency key, trace context, and expected output schema.

The receiving system independently authenticates the caller and checks its own policy. The Controller's plan is not authorization.

### Result envelope

A result returns request/correlation IDs, output artifact IDs/digests, execution status/timestamps, tool/system versions, evidence links, verification status and verifier identity/version, limitations, unresolved questions, and any required human disposition.

## 5. Controller lifecycle

1. Receive and register request/artifacts.
2. Identify task type and required scope; preserve ambiguity.
3. Retrieve only authorized capability descriptors and evidence.
4. Produce a plan from explicitly selected, registered capabilities.
5. Check availability and whether evidence status supports the proposed use.
6. Obtain required external human authorization before protected side effects.
7. Dispatch through the Bridge only after independent enforcement at caller and receiver.
8. Collect result envelopes and register outputs/lineage.
9. Invoke independent verification appropriate to each claim.
10. Present evidence, limitations, and disposition for required human decision.

The current KHGSI kernel implements only planning. It does not implement the integrated production workflow.

## 6. Trust boundaries and failure behavior

Original artifacts are immutable; derived outputs have new identities. Untrusted inputs are parsed in bounded contexts. Shared data is retrieved by explicit scope, not ambient authority. Cross-system messages are authenticated, authorized, validated, and logged. Credentials are scoped, revocable, and never stored in plaintext source control. Controller, Bridge, security, and ledger have independent failure domains. Research artifacts enter engineering only through controlled evidence-bearing transfer and required disposition.

Missing authorization, unknown capability, incompatible policy, invalid signature, untrusted artifact, failed integrity check, unavailable dependency, or unresolved high-risk condition must fail closed for the affected operation. Preserve evidence and report a precise status.
