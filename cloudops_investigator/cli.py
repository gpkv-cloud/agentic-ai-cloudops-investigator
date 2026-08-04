"""Command-line interface for the CloudOps investigator."""

from __future__ import annotations

import argparse
from pathlib import Path

from cloudops_investigator.investigator import investigate
from cloudops_investigator.reporting import format_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="cloudops-investigator",
        description="Read-only Agentic AI CloudOps incident investigator.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    investigate_parser = subparsers.add_parser(
        "investigate",
        help="Investigate an incident using read-only mock data.",
    )
    investigate_parser.add_argument(
        "question",
        help="Incident question or symptom to investigate.",
    )
    investigate_parser.add_argument(
        "--data-dir",
        default="mock_data",
        help="Directory containing mock investigation data.",
    )

    args = parser.parse_args(argv)

    if args.command == "investigate":
        report = investigate(args.question, data_dir=Path(args.data_dir))
        print(format_report(report))
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2
