# Ketchum Human-Governed Superintelligence Ecosystem (KHGSI)

**Identity:** Unified Human-Governed Superintelligence Ecosystem  
**Version:** 0.1.0  
**Status:** FOUNDATIONAL SPECIFICATION + EXPERIMENTAL PLANNING KERNEL — NOT QUALIFIED, NOT PRODUCTION-READY, NOT RATIFIED

**Clone source:** Evank253/Seed-bank- @ a9cf53d19c31bcdc38c7c45a89c374fee8664d70  
**Location in this roof:** systems/khgsi/ (additive clone only — original Seed Bank untouched)

KHGSI is a federated architecture of independent intelligence, engineering, scientific, assurance, governance, data, and defensive systems. It coordinates collaboration while preserving each participant's identity, responsibility, security boundary, and permission scope.

This is not a monolithic AI application and is not a claim that superintelligence or every intended capability has been achieved.

## Governing principle

**Intelligence without self-sovereignty. Autonomy without unrestricted authority. Federation without surrendering independence.**

External Human Authority remains outside every software component. The designated External Human Authority is Evan Ketchum. No software component can create, grant, modify, replace, impersonate, or assume that authority.

## Contents

- KHGSI-001-FOUNDATIONAL-DOCTRINE.md — constitutional and operating invariants.
- KHGSI-002-REFERENCE-ARCHITECTURE.md — system boundaries and information flows.
- KHGSI-003-CAPABILITY-REGISTRY.json — evidence-qualified Seed Bank capability inventory.
- KHGSI-004-INTEGRATION-ROADMAP.md — staged implementation and acceptance gates.
- khgsi/ — callable, registry-driven planning kernel.
- tests/ and run_tests.py — foundation tests.

## Call the planning kernel (from this repository root)

```bash
PYTHONPATH=systems/khgsi python -m khgsi plan \
  --registry systems/khgsi/KHGSI-003-CAPABILITY-REGISTRY.json \
  --task-id TASK-001 \
  --capability URSIE-INTAKE-001 \
  --capability PROMETHEUS-INTERPRET-001
```

The command creates a capability participation plan. It does not invoke tools, grant permissions, approve work, or execute tasks. Only explicitly requested capability IDs are considered. Unknown, unimplemented, or non-callable capabilities are blocked.

Run tests:

```bash
python systems/khgsi/run_tests.py
```

## Current boundary

The kernel is planning-only. It is not the production Central Controller. It has no live KCN, federation, KCN Link Bridge, shared Data Layer, cyber-defense, Preflight, AHM, research-lab, or business-application integrations.

The registry distinguishes Seed Bank evidence from external-repository evidence not inspected in this pass. A name in the doctrine does not make a system implemented. A callable entry point is not proof of qualification or production safety.

The kernel has no authority-bearing identity and cannot establish a HumanReceipt. A plan is not authorization or execution. Test success is not qualification or ratification.
