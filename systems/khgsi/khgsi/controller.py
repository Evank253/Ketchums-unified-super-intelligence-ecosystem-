"""KHGSI registry-driven planning kernel.

Plans capability participation only. It does not execute tools, grant
permissions, verify human authority, or modify external systems.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
import json

CALLABLE_STATUSES = {
    "IMPLEMENTED",
    "LIMITED_IMPLEMENTED",
    "IMPLEMENTED_EXPERIMENTAL_NOT_QUALIFIED",
}


class RegistryError(ValueError):
    """Raised when a capability registry is malformed or unsupported."""


@dataclass(frozen=True)
class Capability:
    capability_id: str
    name: str
    system_id: str
    status: str
    domains: tuple[str, ...]
    invocation: str | None
    limitations: tuple[str, ...]

    @property
    def callable_reference(self) -> bool:
        return self.status in CALLABLE_STATUSES and bool(self.invocation)


@dataclass(frozen=True)
class PlanResult:
    task_id: str
    selected: tuple[str, ...]
    blocked: tuple[dict[str, str], ...]

    def to_dict(self) -> dictdict[str, Any]:
        return {
            "task_id": self.task_id,
            "selected_capabilities": list(self.selected),
            "blocked_capabilities": [dict(item) for item in self.blocked],
            "execution_status": "NOT_EXECUTED",
            "authority_status": "NOT_ESTABLISHED_BY_KERNEL",
            "controller_limit": "PLANNING_ONLY_NO_TOOL_DISPATCH",
        }


def load_registry_data(data: dict[str, Any]) -> dict[str, Capability]:
    if data.get("schema") != "KHGSI-CAPABILITY-REGISTRY-1":
        raise RegistryError("Unsupported or missing registry schema")
    rows = data.get("capabilities")
    if not isinstance(rows, list):
        raise RegistryError("capabilities must be a list")

    registry: dict[str, Capability] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise RegistryError("Each capability entry must be an object")
        required = ("capability_id", "name", "system_id", "status")
        if any(not isinstance(row.get(key), str) or not row[key].strip() for key in required):
            raise RegistryError("Every capability requires non-empty ID, name, system ID, and status")

        capability_id = row["capability_id"]
        if capability_id in registry:
            raise RegistryError(f"Duplicate capability_id: {capability_id}")

        domains = row.get("domains", [])
        limitations = row.get("limitations", [])
        invocation = row.get("invocation")
        if not isinstance(domains, list) or not all(isinstance(value, str) for value in domains):
            raise RegistryError(f"Invalid domains for {capability_id}")
        if not isinstance(limitations, list) or not all(isinstance(value, str) for value in limitations):
            raise RegistryError(f"Invalid limitations for {capability_id}")
        if invocation is not None and not isinstance(invocation, str):
            raise RegistryError(f"Invalid invocation for {capability_id}")

        registry[capability_id] = Capability(
            capability_id, row["name"], row["system_id"], row["status"],
            tuple(domains), invocation, tuple(limitations),
        )
    return registry


def load_registry(path: str | Path) -> dict[str, Capability]:
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RegistryError(f"Cannot load capability registry: {exc}") from exc
    if not isinstance(data, dict):
        raise RegistryError("Registry root must be an object")
    return load_registry_data(data)


def plan_task(
    task_id: str,
    required_capability_ids: Iterable[str],
    registry: dict[str, Capability],
) -> PlanResult:
    """Create a deterministic plan from explicit IDs; never dispatch or execute."""
    if not isinstance(task_id, str) or not task_id.strip():
        raise ValueError("task_id must be a non-empty string")
    requested = list(required_capability_ids)
    if not requested:
        raise ValueError("At least one explicit capability ID is required")
    if any(not isinstance(value, str) or not value.strip() for value in requested):
        raise ValueError("Capability IDs must be non-empty strings")
    if len(requested) != len(set(requested)):
        raise ValueError("Duplicate requested capability IDs are not allowed")

    selected: list[str] = []
    blocked: list[dict[str, str]] = []
    for capability_id in requested:
        capability = registry.get(capability_id)
        if capability is None:
            blocked.append({"capability_id": capability_id, "reason": "NOT_REGISTERED"})
        elif not capability.callable_reference:
            blocked.append({
                "capability_id": capability_id,
                "reason": f"STATUS_NOT_CALLABLE:{capability.status}",
            })
        else:
            selected.append(capability_id)
    return PlanResult(task_id, tuple(selected), tuple(blocked))
