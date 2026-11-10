# Unified Capability Registry

**Purpose:** Structured description of systems that may participate in the federated ecosystem.  
**Rule:** Entry in this registry does not grant execution rights. Authorization remains external and per-request.  
**Mode:** Read-only discovery first. Execution only after explicit human authorization and verification.

## Registry Schema (per capability)

| Field | Purpose |
|-------|---------|
| System ID | Identifies the system |
| Capability ID | Identifies a particular function |
| Interface | How it can be invoked |
| Input schema | Acceptable inputs |
| Output schema | Expected outputs |
| Permission scope | Who can request execution |
| Dependencies | Required systems |
| Security requirements | Protective controls |
| Verification status | Actual testing status |
| Version | Implementation version |
| Evidence | Links to supporting records |
| Source repository | External, unmodified source |
| Integration status | NOT_CONNECTED / READ_ONLY / AUTHORIZED / VERIFIED |

## Core Systems (External References)

### Intelligence Family

| System ID | Role | Source Repository | Integration Status |
|-----------|------|-------------------|--------------------|
| PROMETHEUS-UEII | Universal Engineering & Intelligence Interface (translation, reconstruction, specification) | Evank253/Seed-bank- (017-UNIVERSAL-ENGINEERING-INTELLIGENCE-INTERFACE) | SNAPSHOT_REFERENCED |
| BUILDER-NL | Natural Language Builder / Bilingual Interpreter | Seed Bank + related Builder work | NOT_CONNECTED |
| SOLVER-UNIVERSAL | Universal Solver (mathematical, logical, computational) | Related solver / OMNISOLVER records | NOT_CONNECTED |
| SCI-INTEL | Scientific Intelligence Laboratory | MANIFEX-ART-SCIENTIFIC-INTELLIGENCE and related | NOT_CONNECTED |
| KCN-II | Ketchum's Intelligent Investigator | Evank253/KCN-II | NOT_CONNECTED |

### Engineering Family

| System ID | Role | Source Repository | Integration Status |
|-----------|------|-------------------|--------------------|
| MANIFEX | Engineering Intelligence & Execution OS | Evank253/MANIFEX | NOT_CONNECTED |
| MANIFEX-MILLENNIUM | Engineering / scientific discovery layer | Evank253/Manifex-millennium- | NOT_CONNECTED |
| VIBE-CODER | Execution / coding engine | Related Vibe / Kronos work | NOT_CONNECTED |
| VIBE-DEVELOPER | Packaging / clean / deploy preparation | Evank253/vibe-developer | NOT_CONNECTED |
| AHM | Authorized Healing / repair proposals | Doctrine references | NOT_CONNECTED |

### Governance Family

| System ID | Role | Source Repository | Integration Status |
|-----------|------|-------------------|--------------------|
| KCN-CORE | Cognitive and governance infrastructure | Evank253/KCN-SUPER-COGNITIVE-HUMAN-GOVERNED-INTELLIGENCE-ECOSYSTEM- | NOT_CONNECTED |
| PRIMORDIAL-RULE | Foundational immutable restrictions | Evank253/kcn-clone-primordial-rule (isolated) | NOT_CONNECTED |
| FEDERATION | Membership, permissions, trust | Doctrine + business scaffolds | NOT_CONNECTED |
| CONTROLLER | Orchestration above independent roots | Evank253/kcn-clone-controller (isolated) | NOT_CONNECTED |

### Infrastructure Family

| System ID | Role | Source Repository | Integration Status |
|-----------|------|-------------------|--------------------|
| KCN-LINK | Interoperability bridge (Terra Nullius pattern) | Evank253/kcn-clone-bridge + KCN Link doctrine | NOT_CONNECTED |
| DATA-LAYER | Shared memory, artifact storage, provenance | Related data / evidence roots | NOT_CONNECTED |
| SEED-BANK | Preserved knowledge, ancestry, reusable discoveries | Evank253/Seed-bank- | READ_ONLY_REFERENCE |
| GENESIS-SEED | Foundational seed lineage | Seed Bank 004 / 005 | READ_ONLY_REFERENCE |

### Assurance Family

| System ID | Role | Source Repository | Integration Status |
|-----------|------|-------------------|--------------------|
| PREFLIGHT | Inspection, validation, testing, assurance | Evank253/kcn-preflight | NOT_CONNECTED |
| EVIDENCE-LEDGER | Append-only evidence and verification records | Multiple evidence roots | NOT_CONNECTED |
| CI-GATES | Live CI and branch protection | Per-repo CI | NOT_CONNECTED |

### Security Family

| System ID | Role | Source Repository | Integration Status |
|-----------|------|-------------------|--------------------|
| CYBER-DEFENSE | Individual, inter-system, and ecosystem protection | Related cyber / security fabric work | NOT_CONNECTED |
| SECURITY-FABRIC | YARA, GovernanceStore, evidence mapping | Isolated clone security roots | NOT_CONNECTED |

### Business Surface

| System ID | Role | Source Repository | Integration Status |
|-----------|------|-------------------|--------------------|
| NEW-BUSINESS | Live business application scaffold | Evank253/MANIFEX-MILLENNIUM-NEW-BUSINESS | NOT_CONNECTED |
| BUSINESS-FINAL | Architectural continuity and recovered knowledge | Evank253/The-unified-Manifex-millennium-full-business-final- | READ_ONLY_REFERENCE |

## Notes

- `NOT_CONNECTED` means no live adapter or authorization path has been established in this repository.
- `READ_ONLY_REFERENCE` means documentation and identifiers are recorded; no write path exists.
- `SNAPSHOT_REFERENCED` means a bounded, attributed snapshot of the Prometheus interface material is preserved under this roof for investigation and architecture work only.
- No capability listed here is authorized for autonomous execution by virtue of appearing in the registry.
