# Beginner Learning Roadmap

This roadmap explains what you will learn at each step.

## Step 1: Understand CloudOps Incident Investigation

What we do:

- Learn what an incident is.
- Learn what engineers check during an incident.
- Pick one simple incident scenario.

What you learn:

- CloudOps basics
- Incident response basics
- Why logs, metrics, and events matter

Example:

```text
Payment service is returning 500 errors.
```

## Step 2: Understand Agentic AI

What we do:

- Learn the difference between a chatbot and an agent.
- Understand how an AI agent uses tools.

What you learn:

- Agent
- Tool calling
- Reasoning workflow
- Evidence collection

Simple idea:

```text
Chatbot = answers questions
Agent = decides steps, uses tools, and completes a task
```

## Step 3: Create Mock Data

What we do:

- Create fake logs.
- Create fake metrics.
- Create fake Kubernetes events.
- Create fake runbooks.

What you learn:

- How production data looks
- How to test without real AWS
- How to keep the first version simple

Why mock data first:

- No cloud cost
- No credentials needed
- Easy to understand
- Easy to test

## Step 4: Build Read-Only Tools

What we do:

- Create functions that read mock data.

Example tools:

```text
get_logs(service_name)
get_metrics(service_name)
get_kubernetes_events(service_name)
search_runbooks(query)
```

What you learn:

- How agents access data
- How to design safe tools
- How to separate data collection from AI reasoning

## Step 5: Build The Investigation Workflow

What we do:

- Build the logic that decides what to check first, second, and third.

What you learn:

- Agent workflow design
- Incident investigation sequence
- Evidence correlation

Workflow:

```text
User reports issue
-> Agent identifies service
-> Agent checks logs
-> Agent checks metrics
-> Agent checks events
-> Agent searches runbook
-> Agent creates report
```

## Step 6: Generate A Report

What we do:

- Convert evidence into a clear report.

What you learn:

- Incident report structure
- Root cause explanation
- Confidence scoring
- Clear communication

Report sections:

- Summary
- Evidence
- Timeline
- Likely root cause
- Confidence
- Recommended next steps

## Step 7: Add A CLI

What we do:

- Run the project from the terminal.

Example:

```bash
python -m cloudops_investigator investigate "payment service has 500 errors"
```

What you learn:

- Command-line tools
- Python project structure
- Local project execution

## Step 8: Add Tests

What we do:

- Create test incidents and expected results.

What you learn:

- Unit testing
- Scenario testing
- How to make an AI workflow reliable

Example:

```text
If logs show database timeout and metrics show high error rate,
the report should mention database connection issue.
```

## Step 9: Add AWS Integrations Later

What we do:

- Replace mock tools with real read-only AWS tools.

Possible AWS services:

- CloudWatch Logs
- CloudWatch Metrics
- CloudWatch Alarms
- CloudTrail
- EKS
- ALB
- RDS

What you learn:

- AWS monitoring
- Read-only IAM permissions
- Real-world CloudOps investigation

## Step 10: Add A Dashboard Later

What we do:

- Add a web UI after the backend works.

What you learn:

- Frontend and backend connection
- Incident dashboard design
- User experience for CloudOps tools

## Best Learning Rule

Build one small working version first.

Do not start with real AWS, real Kubernetes, or a complex UI. First understand the agent flow using mock data.
