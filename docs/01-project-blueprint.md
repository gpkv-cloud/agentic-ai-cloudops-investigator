# Project Blueprint

## Project Name

Agentic AI CloudOps Investigator

## Simple Explanation

This project is an AI assistant that helps investigate cloud incidents.

An incident means something is wrong in a system, such as:

- API is returning errors
- Website is slow
- Service is down
- Kubernetes pods are restarting
- Database connections are failing

The assistant will not fix the issue automatically. It will only investigate and explain what it finds.

## Main Use Case

The first use case is:

```text
Payment service is returning 500 errors after a deployment.
```

The investigator should answer:

- What is failing?
- When did it start?
- What evidence supports the finding?
- What is the likely root cause?
- What should a human engineer check next?

## User

The user is a CloudOps, DevOps, SRE, or AWS engineer.

This user wants help during incident investigation, especially when there are many places to check.

## What The Agent Reads

The agent will read data from:

- Application logs
- Metrics
- Kubernetes events
- AWS events
- Runbooks

For the first version, these will be mock files stored inside the project.

Later, these can be replaced with real integrations.

## What The Agent Does Not Do

The agent must not:

- Restart services
- Delete pods
- Change AWS resources
- Modify Kubernetes resources
- Deploy code
- Change security groups
- Change databases

This is important because AI systems should not make infrastructure changes without human approval.

## Final Output

The final output should look like an incident investigation report:

```text
Incident Summary:
Payment service is returning 500 errors.

Evidence:
- Logs show database connection timeout errors.
- Metrics show error rate increased after deployment.
- Kubernetes pods are running, but restart count increased.
- Runbook matches database connection exhaustion.

Likely Root Cause:
Database connection pool issue after deployment.

Confidence:
High

Recommended Next Steps:
- Human engineer should check database connection pool settings.
- Human engineer should compare the latest deployment changes.
```

## Why This Is A Good Agentic AI Project

This project is useful because it combines:

- AI reasoning
- Tool usage
- CloudOps knowledge
- AWS investigation
- Kubernetes investigation
- Safety rules
- Evidence-based reporting

It is more practical than a simple chatbot because the AI has a clear job and uses tools to complete it.
