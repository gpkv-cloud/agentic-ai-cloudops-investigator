"""Report formatting for investigation results."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Evidence:
    """One finding collected during an investigation."""

    source: str
    message: str
    severity: str = "info"


@dataclass(frozen=True)
class InvestigationReport:
    """Final report returned by the investigator."""

    incident_title: str
    service: str
    summary: str
    evidence: list[Evidence] = field(default_factory=list)
    likely_root_cause: str = "Unknown"
    confidence: str = "Low"
    recommended_next_steps: list[str] = field(default_factory=list)


def format_report(report: InvestigationReport) -> str:
    """Format an investigation report for terminal output."""
    lines = [
        f"Incident: {report.incident_title}",
        f"Service: {report.service}",
        "",
        "Summary:",
        report.summary,
        "",
        "Evidence:",
    ]

    for item in report.evidence:
        lines.append(f"- [{item.source}] {item.message}")

    lines.extend(
        [
            "",
            "Likely Root Cause:",
            report.likely_root_cause,
            "",
            "Confidence:",
            report.confidence,
            "",
            "Recommended Human Next Steps:",
        ]
    )

    for step in report.recommended_next_steps:
        lines.append(f"- {step}")

    return "\n".join(lines)
