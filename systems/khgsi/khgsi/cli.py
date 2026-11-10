"""CLI for the KHGSI planning-only kernel."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .controller import load_registry, plan_task


def main() -> int:
    parser = argparse.ArgumentParser(description="KHGSI planning-only capability coordinator")
    subparsers = parser.add_subparsers(dest="command", required=True)
    plan = subparsers.add_parser("plan", help="create a non-executing capability plan")
    plan.add_argument("--registry", required=True, type=Path)
    plan.add_argument("--task-id", required=True)
    plan.add_argument("--capability", action="append", required=True, dest="capabilities")
    args = parser.parse_args()
    registry = load_registry(args.registry)
    result = plan_task(args.task_id, args.capabilities, registry)
    print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
