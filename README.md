# Agentic AI CloudOps Investigator

Read-only Agentic AI assistant for CloudOps incident investigation using logs, Kubernetes data, metrics, and runbooks.

## What This Project Does

This project will help a CloudOps or DevOps engineer investigate production incidents.

Example:

```text
Payment service is returning 500 errors.
```

The AI investigator will collect evidence from read-only sources:

- Logs
- Metrics
- Kubernetes or EKS status
- AWS signals such as CloudWatch and CloudTrail
- Runbooks

Then it will produce an incident investigation report with:

- Summary
- Evidence
- Timeline
- Likely root cause
- Confidence level
- Recommended human next steps

## Important Safety Rule

This project is read-only.

The agent can inspect systems, but it must not restart pods, delete resources, deploy code, change infrastructure, or modify cloud configuration.

## Beginner Build Order

We will build this project step by step:

1. Understand the use case and scope.
2. Create mock incident data.
3. Build read-only tool functions.
4. Build the investigation agent workflow.
5. Generate incident reports.
6. Add a command-line interface.
7. Add tests.
8. Add real AWS and Kubernetes integrations later.
9. Optionally add a web dashboard.

## How To Run

This first version uses only the Python standard library.

From the project folder, run:

```bash
python -m cloudops_investigator investigate "payment service is returning 500 errors"
```

Run tests:

```bash
python -m unittest discover -s tests
```

If `python` is not installed or not available in your terminal, install Python 3.10 or newer and then run the commands again.

## What Exists Now

```text
cloudops_investigator/
  cli.py            command-line interface
  investigator.py   first deterministic investigation workflow
  reporting.py      incident report model and formatter
  tools.py          read-only mock data tools

mock_data/
  incidents/        incident description
  logs/             fake application logs
  metrics/          fake service metrics
  kubernetes/       fake Kubernetes workload and events
  runbooks/         fake troubleshooting runbook

tests/
  test_investigator.py
```

## Documentation

Start here:

- [Project Blueprint](docs/01-project-blueprint.md)
- [Beginner Learning Roadmap](docs/02-beginner-learning-roadmap.md)
- [Architecture](docs/03-architecture.md)
- [MVP Build Plan](docs/04-mvp-build-plan.md)
- [Code Walkthrough](docs/05-code-walkthrough.md)

## Current Status

Current phase: local mock-data MVP.

Completed:

- Beginner project documentation
- Mock incident data for `payment-service`
- Read-only mock data tools
- Deterministic investigation workflow
- CLI command
- Unit tests

Not added yet:

- AWS integration
- Kubernetes integration
- LLM integration
- Web dashboard
