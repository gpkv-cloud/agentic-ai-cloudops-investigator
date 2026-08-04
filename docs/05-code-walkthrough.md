# Code Walkthrough

This document explains the first working version in beginner-friendly terms.

## Big Picture

The project now works like this:

```text
Terminal command
-> CLI
-> Investigator workflow
-> Read-only tools
-> Mock data files
-> Evidence
-> Final report
```

## 1. CLI

File:

```text
cloudops_investigator/cli.py
```

Purpose:

The CLI lets you run the project from the terminal.

Command:

```bash
python -m cloudops_investigator investigate "payment service is returning 500 errors"
```

What it does:

1. Reads your incident question.
2. Calls the investigation workflow.
3. Prints the final report.

## 2. Investigation Workflow

File:

```text
cloudops_investigator/investigator.py
```

Purpose:

This is the first version of the agent.

It is deterministic, which means it follows a fixed sequence:

```text
read incident
read logs
read metrics
read Kubernetes events
search runbooks
analyze evidence
return report
```

Why we start this way:

- It is easier to understand.
- It is easier to test.
- It is safer than starting with complex AI behavior.

Later, we can add LLM reasoning on top of this structure.

## 3. Read-Only Tools

File:

```text
cloudops_investigator/tools.py
```

Purpose:

Tools read investigation data.

Current tools:

```text
get_incident()
get_logs()
get_metrics()
get_kubernetes_events()
search_runbooks()
```

Important:

These tools only read local mock files. They do not modify anything.

This is the safety foundation of the project.

## 4. Report Formatting

File:

```text
cloudops_investigator/reporting.py
```

Purpose:

This file defines the final report structure.

Report sections:

- Incident
- Service
- Summary
- Evidence
- Likely root cause
- Confidence
- Recommended human next steps

## 5. Mock Data

Folder:

```text
mock_data/
```

Purpose:

Mock data lets us learn and test without real AWS or Kubernetes access.

Current scenario:

```text
Payment service is returning 500 errors after deployment.
```

The evidence points to:

```text
Database connection pool exhaustion after the latest deployment.
```

## 6. Tests

File:

```text
tests/test_investigator.py
```

Purpose:

Tests confirm that the project works correctly.

They check:

- Logs can be read.
- Metrics can be read.
- Runbook search works.
- Investigator finds the likely root cause.
- Report output contains the important sections.

Run tests:

```bash
python -m unittest discover -s tests
```

## What You Learned In This MVP

You learned:

- How an Agentic AI project can be structured.
- Why agents need tools.
- Why read-only safety matters in CloudOps.
- How logs, metrics, Kubernetes events, and runbooks become evidence.
- How to turn evidence into an incident report.

## What Comes Next

Next recommended step:

```text
Add an LLM layer that explains the evidence in more natural language.
```

After that:

```text
Add real AWS read-only connectors.
```
