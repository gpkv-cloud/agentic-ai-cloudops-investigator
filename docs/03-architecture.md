# Architecture

## Simple Architecture

```text
User
 |
 v
Incident Question
 |
 v
Investigation Agent
 |
 +--> Logs Tool
 |
 +--> Metrics Tool
 |
 +--> Kubernetes Events Tool
 |
 +--> Runbook Search Tool
 |
 v
Evidence Collection
 |
 v
Incident Report
```

## Main Parts

## 1. User Input

The user describes the incident.

Example:

```text
Payment service is returning 500 errors.
```

The agent should understand:

- Which service is affected
- What symptom is reported
- What kind of checks are needed

## 2. Investigation Agent

The investigation agent is the brain of the project.

It decides:

- Which tool to call
- What evidence matters
- Whether more checks are needed
- What the likely root cause is

For the first version, this can be a simple rule-based workflow.

Later, we can add LLM-based reasoning.

## 3. Read-Only Tools

Tools are functions that collect information.

Example:

```text
get_logs("payment-service")
get_metrics("payment-service")
get_kubernetes_events("payment-service")
search_runbooks("database timeout")
```

The agent uses tools, but the tools only read data.

## 4. Mock Data Layer

In the first version, the tools read mock files.

Example mock files:

```text
mock_data/logs/payment-service.log
mock_data/metrics/payment-service.json
mock_data/kubernetes/payment-service-events.json
mock_data/runbooks/database-timeout.md
```

This lets us learn and test without real cloud access.

## 5. Evidence Collection

The agent collects useful findings from every tool.

Example evidence:

```text
Logs show database timeout errors.
Metrics show error rate increased after deployment.
Kubernetes events show pod restarts.
Runbook matches database connection exhaustion.
```

## 6. Incident Report

The final report explains the incident clearly.

Report sections:

- Incident summary
- Evidence
- Timeline
- Likely root cause
- Confidence
- Recommended human next steps

## Future Real AWS Architecture

After the mock version works, the same structure can connect to AWS:

```text
Investigation Agent
 |
 +--> CloudWatch Logs
 +--> CloudWatch Metrics
 +--> CloudWatch Alarms
 +--> CloudTrail
 +--> EKS
 +--> ALB
 +--> RDS
 +--> Runbooks
```

The important design stays the same:

```text
Agent decides what to check.
Tools collect read-only evidence.
Report explains the finding.
```
