# Mock Data

This folder contains fake incident data for learning and testing.

We use mock data first so the project can run without:

- AWS credentials
- A real Kubernetes cluster
- Cloud cost
- Production risk

## Current Incident Scenario

```text
Payment service is returning 500 errors after a deployment.
```

The data is split into the same types of sources a CloudOps engineer would normally check:

- `incidents/` contains the incident description.
- `logs/` contains application log lines.
- `metrics/` contains service and database metrics.
- `kubernetes/` contains pod and event information.
- `runbooks/` contains troubleshooting documentation.

The future investigation agent will read these files through read-only tool functions.
