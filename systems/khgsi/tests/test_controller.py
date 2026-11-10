import unittest

from khgsi.controller import RegistryError, load_registry_data, plan_task


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.registry = load_registry_data({
            "schema": "KHGSI-CAPABILITY-REGISTRY-1",
            "capabilities": [
                {"capability_id": "PROM-001", "name": "Prometheus",
                 "system_id": "PROMETHEUS",
                 "status": "IMPLEMENTED_EXPERIMENTAL_NOT_QUALIFIED",
                 "domains": ["bounded-interpretation"], "invocation": "python module",
                 "limitations": ["bounded patterns"]},
                {"capability_id": "OMNI-001", "name": "OmniSolver", "system_id": "OMNI",
                 "status": "PROPOSED_NOT_IMPLEMENTED", "domains": ["complexity"],
                 "invocation": None, "limitations": ["not implemented"]},
            ],
        })

    def test_plans_callable_reference_without_execution(self):
        result = plan_task("TASK-1", ["PROM-001"], self.registry).to_dict()
        self.assertEqual(result["selected_capabilities"], ["PROM-001"])
        self.assertEqual(result["execution_status"], "NOT_EXECUTED")
        self.assertEqual(result["authority_status"], "NOT_ESTABLISHED_BY_KERNEL")

    def test_unimplemented_capability_is_blocked(self):
        result = plan_task("TASK-2", ["OMNI-001"], self.registry).to_dict()
        self.assertEqual(result["selected_capabilities"], [])
        self.assertEqual(result["blocked_capabilities"][0]["reason"],
                         "STATUS_NOT_CALLABLE:PROPOSED_NOT_IMPLEMENTED")

    def test_unknown_capability_is_blocked(self):
        result = plan_task("TASK-3", ["MISSING"], self.registry).to_dict()
        self.assertEqual(result["blocked_capabilities"][0]["reason"], "NOT_REGISTERED")

    def test_duplicate_registry_ids_are_rejected(self):
        data = {"schema": "KHGSI-CAPABILITY-REGISTRY-1", "capabilities": [
            {"capability_id": "X", "name": "x", "system_id": "s", "status": "IMPLEMENTED"},
            {"capability_id": "X", "name": "y", "system_id": "s", "status": "IMPLEMENTED"}]}
        with self.assertRaises(RegistryError):
            load_registry_data(data)

    def test_invalid_requests_are_rejected(self):
        with self.assertRaises(ValueError):
            plan_task("", ["PROM-001"], self.registry)
        with self.assertRaises(ValueError):
            plan_task("TASK", [], self.registry)
        with self.assertRaises(ValueError):
            plan_task("TASK", ["PROM-001", "PROM-001"], self.registry)


if __name__ == "__main__":
    unittest.main()
