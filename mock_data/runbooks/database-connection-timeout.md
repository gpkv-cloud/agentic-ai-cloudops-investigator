# Runbook: Database Connection Timeout

## Symptoms

- Application logs show database connection timeout.
- HTTP 500 errors increase.
- Request latency increases.
- Database connection utilization is close to 100%.

## Common Causes

- Database connection pool is too small.
- New deployment increased database connection usage.
- Database max connection limit was reached.
- Long-running queries are holding connections.
- Network issue exists between application pods and database.

## Read-Only Checks

1. Check application logs for timeout and connection pool errors.
2. Check service error rate and latency metrics.
3. Check database connection utilization.
4. Check recent deployments or configuration changes.
5. Check Kubernetes events for readiness probe failures.

## Human Next Steps

- Review the latest deployment diff.
- Compare connection pool settings between current and previous version.
- Check database max connection configuration.
- Ask the database owner to inspect long-running queries.
- Rollback only after human approval and normal change process.

## Safety Note

Do not restart, rollback, or modify production resources automatically.
