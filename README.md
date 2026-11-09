# Prometheus — Universal Engineering & Intelligence Interface

**Status:** Initial implementation; experimental, bounded adapters; not yet qualified for production.

Prometheus is being built as a universal engineering and intelligence interface: a shared representation layer between human intent and technical domains. The interface accepts natural-language requests and supported artifacts, produces a provenance-preserving intermediate representation, and translates that representation into bounded technical specifications.

## Core pipeline

`Human language / artifact → parse & inspect → Universal Representation → validate → target adapter → output + evidence`

Reverse reconstruction follows the same path in reverse. Unsupported or ambiguous content is preserved as unresolved rather than guessed.

## Initial capabilities
- English and Spanish input handling for a documented starter vocabulary and request patterns.
- Structured representation of goals, entities, relationships, constraints, operations, assumptions, and unresolved statements.
- Forward specification adapters for JSON, software architecture, algorithm/pseudocode, mathematical expressions, and Python-oriented implementation plans.
- Reverse inspection of JSON, Python source, mathematical expressions, and architecture text.
- Provenance, source digests, confidence boundaries, and explicit evidence states.
- Integration with the Seed Bank semantic relationship builder as an attributed, unchanged source snapshot.

## Important limits
"Universal" describes the extensible architecture and intended coverage, not a claim that the current implementation understands every language, format, scientific domain, or system. Adapters are explicit and versioned. Generated implementation plans are not executed automatically. Mathematical or semantic correctness, security, physical feasibility, and human intent require appropriate independent validation.

## Governance
- Human authority remains external to the software.
- Capability is not evidence, qualification, authority, or ratification.
- No generated plan can authorize its own execution.
- Unknowns remain visible as `UNRESOLVED` / `NOT_MEASURED`.
- Source snapshots are preserved; changes to this repository are additive.

## Run
```bash
python -m unittest discover -s tests -v
python -m prometheus_interface.cli --text "Build a service that validates incoming records" --target architecture
```
