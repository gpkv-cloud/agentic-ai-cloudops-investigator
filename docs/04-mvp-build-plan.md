# MVP Build Plan

MVP means Minimum Viable Product.

It is the smallest useful version of the project.

## MVP Goal

The first working version should investigate one sample incident:

```text
Payment service is returning 500 errors after deployment.
```

It should use mock data and produce a useful report.

## What We Build First

## Step 1: Project Documentation

Status: completed

What we create:

- Project blueprint
- Learning roadmap
- Architecture
- MVP plan

Why:

- You are new to Agentic AI.
- Clear documentation makes the coding easier.
- The GitHub project becomes easier to understand.

## Step 2: Mock Incident Data

Status: completed

What we will create:

```text
mock_data/
  logs/
  metrics/
  kubernetes/
  runbooks/
```

Created first scenario:

```text
Payment service is returning 500 errors after deployment.
```

Files:

```text
mock_data/incidents/payment-service-500-after-deployment.json
mock_data/logs/payment-service.log
mock_data/metrics/payment-service.json
mock_data/kubernetes/payment-service-events.json
mock_data/runbooks/database-connection-timeout.md
```

Why:

- We can test the agent without AWS.
- We can control the incident scenario.

What you learn:

- What logs look like
- What metrics look like
- What Kubernetes events look like
- What runbooks look like

## Step 3: Read-Only Tool Functions

Status: completed

What we will create:

```text
cloudops_investigator/tools/
```

Example tools:

```text
get_logs(service_name)
get_metrics(service_name)
get_kubernetes_events(service_name)
search_runbooks(query)
```

Why:

- Agents need tools to inspect data.
- Tools keep the system organized.

What you learn:

- Tool design
- Read-only safety
- How AI agents collect evidence

## Step 4: Investigation Agent

Status: completed

What we will create:

```text
cloudops_investigator/agent/
```

The first agent will follow a clear sequence:

```text
check logs
check metrics
check Kubernetes events
check runbook
create report
```

Why:

- A beginner-friendly agent should be predictable.
- We can improve it later.

What you learn:

- Agent workflow
- Reasoning sequence
- Evidence correlation

## Step 5: Report Generator

Status: completed

What we will create:

```text
cloudops_investigator/reporting/
```

The report will include:

- Summary
- Evidence
- Likely root cause
- Confidence
- Recommended next steps

Why:

- Investigation is useful only if the output is clear.

What you learn:

- Incident communication
- Root cause explanation
- Report formatting

## Step 6: CLI

Status: completed

What we will create:

```text
python -m cloudops_investigator investigate "payment service has 500 errors"
```

Why:

- A CLI is easier than a web UI for the first version.
- DevOps engineers commonly use terminal tools.

What you learn:

- Python CLI basics
- Running a local project

## Step 7: Tests

Status: completed

What we will create:

```text
tests/
```

Why:

- Tests prove the project works.
- Tests make the project stronger for GitHub.

What you learn:

- Unit tests
- Scenario tests
- How to verify an agent workflow

## What We Will Not Build In The MVP

Not in the first version:

- Real AWS connection
- Real Kubernetes connection
- Web dashboard
- Slack integration
- Automatic remediation

These can come later after the basic agent works.

## MVP Success Criteria

The MVP is successful when:

- A user can enter an incident question. Completed.
- The agent reads mock data. Completed.
- The agent finds useful evidence. Completed.
- The agent creates a clear report. Completed.
- The project can be tested locally. Completed.

## Next Step

The next build step is:

```text
Add beginner-friendly explanation comments and then prepare for optional LLM integration.
```
