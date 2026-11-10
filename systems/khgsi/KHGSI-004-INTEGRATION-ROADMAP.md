# KHGSI-004 — Integration Roadmap and Acceptance Gates

**Status:** Proposed implementation sequence. No production integration is claimed.

## Operating rule

Build around the systems that already exist. Do not replace independent engines with duplicate implementations. Preserve Seed Bank, original MANIFEX, research records, and existing repositories. Repository writes remain additive-only in the authorized Seed Bank location unless separately approved.

## Phase 0 — Evidence baseline and source mapping

Inventory every relevant repository/branch, artifact hash, system/capability, interface, dependency, permission, security boundary, and test. Every claim must link to a file, commit, test result, or be marked NOT_MEASURED / EXTERNAL_REPOSITORY_EVIDENCE_REQUIRED. No capability is inferred from a name or diagram.

## Phase 1 — Shared capability registry

Define stable IDs, versioned input/output schemas, entry points/transports, permission scopes, risk classes, dependencies, security requirements, health status, and evidence. Reject duplicate IDs. Unknown capabilities fail closed. Registry entries cannot create authority.

## Phase 2 — Shared Data Layer and URSIE lineage

Implement shared artifact identity, registration-first intake, immutable originals, derived-artifact lineage, access-controlled storage, retention, signed external checkpoints, and backups.

**Gate:** byte-preservation/hash tests; new identity and parent links for derived outputs; crash recovery, multi-writer, retention, access, and backup behavior independently tested before production.

## Phase 3 — KCN governance and KCN Link Bridge

Integrate authenticated identities, independent authorization at sender and receiver, scoped invocation, revocation, incident handling, and request/result envelopes.

**Gate:** Bridge cannot authorize a request; no ambient cross-system privilege; compromised members cannot automatically compromise peers; OIDC proves identity only; negative tests cover replay, confused deputy, escalation, revocation, malformed payloads, and policy mismatch.

## Phase 4 — Central Controller

Implement capability discovery/planning, dependency-aware workflow graphs, budgets, deadlines, idempotency, retries, cancellation, human checkpoints, result aggregation, and evidence collection.

**Gate:** Controller is not an authority issuer; receivers independently enforce authorization; controller compromise cannot disable governance; unknown/unavailable/unqualified capabilities are not silently invoked. No live dispatch until governance and Bridge gates pass.

## Phase 5 — Intelligence and engineering integrations

Connect the existing Builder/URSIE, Solver, MANIFEX, scientific and mathematical engines, anomaly systems, and other capabilities through versioned adapters.

**Gate:** schemas and provenance verified; domain assumptions preserved; candidate outputs distinguished from verified results; adapter tests and failure modes documented; no production side effect without authorization.

## Phase 6 — Preflight and AHM

Implement incoming/outgoing inspection, finding classification, evidence, scoped repair, checkpoints, immutable before/after artifacts, independent post-repair tests, rollback, and recovery.

**Gate:** AHM cannot approve its own repair; every repair links to finding and source digest; failed attempts preserved; Preflight statuses PASS/FAIL/INCOMPLETE/UNRESOLVED/NOT_MEASURED are accurate.

## Phase 7 — Cybersecurity and defense

Implement per-system security baselines, inter-system transport/identity controls, cross-system detection, credential vaulting, rotation/revocation, quarantine, forensic preservation, and verified recovery.

**Gate:** threat model, attack-surface inventory, negative security tests, independent review, scoped containment authority, and no constitutional bypass. No claim of immunity or production security qualification without evidence.

## Phase 8 — Isolated Scientific Research Laboratory

Implement sandboxed compute/data access, reproducible experiment records, resource/network boundaries, and controlled artifact promotion.

**Gate:** research cannot directly write production; all inputs/outputs registered; simulation labeled simulation; domain-specific reproducibility and independent review.

## Phase 9 — Business application and production readiness

Expose only capabilities whose interfaces, security, authorization, availability, and evidence status support the advertised use.

**Gate:** no simulated telemetry represented as live; no disconnected system represented as integrated; customer isolation, secrets, privacy, incident response, backups, monitoring, and rollback tested; human approval remains external.

## Current implementation boundary

This Seed Bank addition provides the doctrine, reference architecture, evidence-qualified registry, and callable planning-only kernel. It does not provide live federation, production controller, KCN Link Bridge, shared Data Layer, universal translation, general Universal Solver, live Preflight/AHM, production cyber defense, research-lab integration, or business application integration.

The next action is a read-only evidence inventory of designated external repositories, exact branch heads, interfaces, tests, and dependency contracts.
