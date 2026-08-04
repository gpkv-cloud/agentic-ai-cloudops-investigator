"""Deterministic first investigation workflow.

This first version is intentionally simple. It does not use an LLM yet.
That makes the behavior easier to understand, test, and improve.
"""

from __future__ import annotations

from pathlib import Path

from cloudops_investigator import tools
from cloudops_investigator.reporting import Evidence, InvestigationReport


DEFAULT_INCIDENT_FILE = "payment-service-500-after-deployment"


def investigate(
    question: str,
    data_dir: Path | str = tools.DEFAULT_DATA_DIR,
    incident_file: str = DEFAULT_INCIDENT_FILE,
) -> InvestigationReport:
    """Investigate one incident using read-only mock data tools."""
    incident = tools.get_incident(incident_file, data_dir)
    service_name = incident["service"]

    log_lines = tools.get_logs(service_name, data_dir)
    metrics = tools.get_metrics(service_name, data_dir)
    kubernetes = tools.get_kubernetes_events(service_name, data_dir)
    runbooks = tools.search_runbooks("database connection timeout", data_dir)

    evidence: list[Evidence] = []
    evidence.extend(_analyze_logs(log_lines))
    evidence.extend(_analyze_metrics(metrics))
    evidence.extend(_analyze_kubernetes(kubernetes))
    evidence.extend(_analyze_runbooks(runbooks))

    likely_root_cause = _choose_root_cause(evidence)
    confidence = _choose_confidence(evidence)

    return InvestigationReport(
        incident_title=incident["title"],
        service=service_name,
        summary=(
            f"The question was: {question}. The mock investigation found "
            "errors after deployment, high database connection usage, and "
            "Kubernetes readiness failures."
        ),
        evidence=evidence,
        likely_root_cause=likely_root_cause,
        confidence=confidence,
        recommended_next_steps=[
            "Review the latest deployment changes for payment-service.",
            "Compare database connection pool settings between versions 1.18.2 and 1.19.0.",
            "Check database max connection limits and long-running queries.",
            "Use the normal human approval process before rollback or remediation.",
        ],
    )


def _analyze_logs(log_lines: list[str]) -> list[Evidence]:
    findings: list[Evidence] = []
    joined_logs = "\n".join(log_lines).lower()

    if "deployment completed" in joined_logs:
        findings.append(
            Evidence(
                source="logs",
                message="Deployment completed before the error spike.",
            )
        )

    if "database connection timeout" in joined_logs:
        findings.append(
            Evidence(
                source="logs",
                message="Application logs show database connection timeout errors.",
                severity="warning",
            )
        )

    if "connection pool exhausted" in joined_logs:
        findings.append(
            Evidence(
                source="logs",
                message="Application logs show the database connection pool reached its maximum.",
                severity="critical",
            )
        )

    if "http 500" in joined_logs:
        findings.append(
            Evidence(
                source="logs",
                message="Application logs show HTTP 500 responses from the payment API.",
                severity="critical",
            )
        )

    return findings


def _analyze_metrics(metrics: dict) -> list[Evidence]:
    findings: list[Evidence] = []
    metric_values = metrics.get("metrics", {})

    error_rate = _last_value(metric_values, "http_5xx_rate_percent")
    if error_rate is not None and error_rate >= 10:
        findings.append(
            Evidence(
                source="metrics",
                message=f"HTTP 5xx rate increased to {error_rate}%.",
                severity="critical",
            )
        )

    latency = _last_value(metric_values, "p95_latency_ms")
    if latency is not None and latency >= 1000:
        findings.append(
            Evidence(
                source="metrics",
                message=f"P95 latency increased to {latency} ms.",
                severity="warning",
            )
        )

    db_connections = _last_value(
        metric_values, "database_connection_utilization_percent"
    )
    if db_connections is not None and db_connections >= 90:
        findings.append(
            Evidence(
                source="metrics",
                message=(
                    "Database connection utilization is high "
                    f"at {db_connections}%."
                ),
                severity="critical",
            )
        )

    return findings


def _analyze_kubernetes(kubernetes: dict) -> list[Evidence]:
    findings: list[Evidence] = []

    workload = kubernetes.get("workload", {})
    current_image = workload.get("current_image")
    previous_image = workload.get("previous_image")
    if current_image and previous_image:
        findings.append(
            Evidence(
                source="kubernetes",
                message=(
                    "Workload is running a new image: "
                    f"{current_image}, previous image was {previous_image}."
                ),
            )
        )

    warning_events = [
        event
        for event in kubernetes.get("events", [])
        if event.get("type", "").lower() == "warning"
    ]
    for event in warning_events:
        findings.append(
            Evidence(
                source="kubernetes",
                message=f"{event.get('reason')}: {event.get('message')}",
                severity="warning",
            )
        )

    return findings


def _analyze_runbooks(runbooks: list[dict]) -> list[Evidence]:
    if not runbooks:
        return []

    best_match = runbooks[0]
    return [
        Evidence(
            source="runbook",
            message=f"Matched troubleshooting guide: {best_match['title']}.",
        )
    ]


def _last_value(metric_values: dict, metric_name: str) -> float | int | None:
    series = metric_values.get(metric_name, [])
    if not series:
        return None
    return series[-1].get("value")


def _choose_root_cause(evidence: list[Evidence]) -> str:
    messages = " ".join(item.message.lower() for item in evidence)
    if "connection pool" in messages and "database connection utilization" in messages:
        return "Database connection pool exhaustion after the latest deployment."
    if "database connection timeout" in messages:
        return "Database connectivity or connection pool issue."
    return "Unknown. More evidence is needed."


def _choose_confidence(evidence: list[Evidence]) -> str:
    critical_count = sum(1 for item in evidence if item.severity == "critical")
    warning_count = sum(1 for item in evidence if item.severity == "warning")

    if critical_count >= 3 and warning_count >= 2:
        return "High"
    if critical_count >= 1:
        return "Medium"
    return "Low"
