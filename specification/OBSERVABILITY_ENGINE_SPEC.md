# Observability Engine Specification

> You cannot intelligently manage what you cannot observe.

Version: 1.0 (Draft)

---

# Purpose

The Observability Engine provides Sentinel with a unified understanding of infrastructure health and behavior.

Rather than treating logs, metrics, traces, telemetry, and alerts as separate systems, the Observability Engine normalizes them into a common operational model.

Its purpose is to answer:

* What is happening?
* Why is it happening?
* Is it normal?
* What changed?
* What is likely to happen next?

---

# Philosophy

Monitoring tells you when something happened.

Observability helps explain why.

The Observability Engine exists to collect signals, correlate them, enrich them with context, and provide meaningful information to the Knowledge Engine and Intelligence Engine.

---

# Core Responsibilities

The Observability Engine is responsible for:

* Collecting telemetry
* Aggregating metrics
* Parsing logs
* Receiving traces
* Correlating events
* Detecting anomalies
* Calculating health
* Measuring service levels
* Publishing observations
* Supporting root cause analysis

---

# Observability Model

```text
Infrastructure
        │
        ▼
Connectors
        │
        ▼
Observability Engine
        │
 ┌──────┼───────────────┐
 │      │               │
Metrics Logs         Traces
 │      │               │
 └──────┴───────────────┘
        │
        ▼
Knowledge Engine
        │
        ▼
Intelligence Engine
```

---

# Signals

Sentinel recognizes several signal types.

## Metrics

Examples:

* CPU utilization
* Memory usage
* Disk usage
* Interface throughput
* Temperature
* Power consumption
* Optical power
* Battery runtime

---

## Logs

Examples:

* System logs
* Application logs
* Audit logs
* Security logs
* Container logs
* Hypervisor logs

Logs should remain searchable and structured whenever possible.

---

## Traces

Examples:

* API requests
* Workflow execution
* Automation execution
* Plugin execution
* Connector operations

Tracing provides execution visibility across Sentinel.

---

## Events

Events describe meaningful changes.

Examples:

* Asset offline
* Backup completed
* Policy denied
* Automation failed
* User logged in

Events originate from the Event Engine but are consumed by Observability.

---

# Correlation

The Observability Engine should correlate signals.

Example:

High CPU

*

Disk latency

*

Database log errors

↓

Possible storage bottleneck

Rather than presenting isolated symptoms, Sentinel should present operational understanding.

---

# Health Model

Health should be calculated.

Suggested states:

Healthy

Informational

Warning

Degraded

Critical

Offline

Unknown

Health should consider multiple signals rather than a single threshold.

---

# Service Health

Services should inherit health.

Example:

Database degraded

↓

Immich degraded

↓

Photo uploads degraded

↓

Home Workspace updated

This allows Sentinel to understand impact.

---

# Baselines

The Observability Engine should learn normal behavior.

Examples:

Typical CPU

Typical traffic

Typical temperatures

Typical latency

Typical backup duration

Typical login frequency

Baselines improve anomaly detection.

---

# Anomaly Detection

Examples:

Unexpected reboot

Traffic spike

Repeated authentication failures

Temperature drift

Storage latency increase

Optical signal degradation

Anomalies should generate observations, not immediate conclusions.

---

# Root Cause Support

The Observability Engine should provide evidence.

Example:

Symptoms:

Immich unavailable

Database latency

Storage pool degraded

Disk errors

Suggested root cause:

Storage failure

Root cause remains a recommendation, not an assumption.

---

# Time

Every observation should include:

Timestamp

Duration

Frequency

Trend

Historical comparison

Time is essential for operational reasoning.

---

# Retention

Different signal types may have different retention.

Example:

Metrics

30 days

Logs

90 days

Audit

1 year

Critical incidents

Indefinite

Retention should remain configurable.

---

# Search

Users should search across all signals.

Examples:

"Disk failures last month"

"Authentication failures"

"UPS battery"

"Immich outages"

Search should operate semantically whenever possible.

---

# Dashboards and Workspaces

Workspaces consume observations rather than raw metrics.

Examples:

Storage Workspace

↓

Storage health

Capacity trends

Recent incidents

Recommendations

Networking Workspace

↓

Link utilization

Interface errors

Neighbor changes

Optical levels

Workspaces remain contextual.

---

# Intelligence Integration

The Intelligence Engine consumes observations.

It may:

Summarize

Predict

Recommend

Explain

Plan

The Observability Engine provides evidence.

The Intelligence Engine provides reasoning.

---

# Security

Observability data should respect:

RBAC

Policies

Organization boundaries

Audit requirements

Sensitive logs should never bypass authorization.

---

# Extensibility

Plugins may contribute:

Metric collectors

Log parsers

Trace providers

Health calculators

Visualizations

Correlation engines

Future observability technologies should integrate through plugins.

---

# Design Rules

1. Observe everything.
2. Correlate signals.
3. Context is more valuable than raw data.
4. Health is calculated.
5. Baselines improve understanding.
6. Evidence supports conclusions.
7. Search should span all signals.
8. Respect security boundaries.
9. Publish observations.
10. Feed knowledge, not dashboards.

---

# Long-Term Vision

The Observability Engine should become Sentinel's senses.

It continuously watches infrastructure, collects signals, correlates evidence, and provides a complete operational picture.

Rather than overwhelming users with dashboards full of disconnected graphs, Sentinel should transform observations into understanding.

Observability is not about seeing more.

It is about understanding more.
