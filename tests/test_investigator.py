import unittest
from pathlib import Path

from cloudops_investigator.investigator import investigate
from cloudops_investigator.reporting import format_report
from cloudops_investigator.tools import get_logs, get_metrics, search_runbooks


DATA_DIR = Path("mock_data")


class MockDataToolsTest(unittest.TestCase):
    def test_get_logs_reads_payment_service_logs(self) -> None:
        logs = get_logs("payment-service", DATA_DIR)

        self.assertGreater(len(logs), 0)
        self.assertTrue(
            any("database connection timeout" in line for line in logs)
        )

    def test_get_metrics_reads_payment_service_metrics(self) -> None:
        metrics = get_metrics("payment-service", DATA_DIR)

        self.assertEqual(metrics["service"], "payment-service")
        self.assertIn("http_5xx_rate_percent", metrics["metrics"])

    def test_search_runbooks_finds_database_timeout_runbook(self) -> None:
        matches = search_runbooks("database connection timeout", DATA_DIR)

        self.assertGreater(len(matches), 0)
        self.assertEqual(matches[0]["title"], "Runbook: Database Connection Timeout")


class InvestigatorTest(unittest.TestCase):
    def test_investigation_finds_database_connection_root_cause(self) -> None:
        report = investigate(
            "payment service is returning 500 errors",
            data_dir=DATA_DIR,
        )

        self.assertEqual(report.service, "payment-service")
        self.assertEqual(report.confidence, "High")
        self.assertIn("Database connection pool exhaustion", report.likely_root_cause)
        self.assertGreaterEqual(len(report.evidence), 6)

    def test_report_format_contains_key_sections(self) -> None:
        report = investigate(
            "payment service is returning 500 errors",
            data_dir=DATA_DIR,
        )
        output = format_report(report)

        self.assertIn("Incident:", output)
        self.assertIn("Evidence:", output)
        self.assertIn("Likely Root Cause:", output)
        self.assertIn("Recommended Human Next Steps:", output)


if __name__ == "__main__":
    unittest.main()
