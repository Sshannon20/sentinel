# Event Engine Specification

> Events are the heartbeat of Sentinel.

Version: 1.0 (Draft)

---

## Purpose

The Event Engine allows Sentinel to understand change.

Instead of treating infrastructure as static dashboards, Sentinel treats every meaningful change as an event.

Events allow connectors, plugins, automations, dashboards, notifications, audit logs, and artificial intelligence to communicate without being tightly coupled.

---

## Core Philosophy

Everything meaningful should become an event.

Examples:

* Asset discovered
* Asset offline
* Service restarted
* Container crashed
* Backup completed
* User logged in
* Credential used
* Camera motion detected
* UPS battery degraded
* Interface down
* Firmware available
* AI recommendation created
* Automation executed

Events make Sentinel aware of what is happening across the environment.

---

## Event Flow

```text
Infrastructure
    │
Connector
    │
Event Engine
    │
├── Automation Engine
├── Knowledge Engine
├── Intelligence Layer
├── Dashboard
├── Notification System
├── Audit Log
└── API / WebSocket Stream
```

Connectors publish events.

Other systems subscribe to events.

No component should need to directly control another component unless an explicit action is requested.

---

## Event Structure

Every event should have a consistent structure.

```json
{
  "id": "evt_01HZXExample",
  "type": "asset.status.changed",
  "source": "connector.ssh.linux",
  "severity": "warning",
  "timestamp": "2026-07-01T18:30:00Z",
  "organization_id": "org_default",
  "site_id": "site_home",
  "asset_id": "asset_utility_vm",
  "actor": {
    "type": "connector",
    "id": "connector_linux_ssh"
  },
  "data": {
    "previous_status": "online",
    "current_status": "degraded"
  },
  "correlation_id": "corr_01HZXExample",
  "trace_id": "trace_01HZXExample"
}
```

---

## Event Types

Event types should use dot notation.

Examples:

```text
asset.discovered
asset.status.changed
asset.health.changed
service.started
service.stopped
service.restarted
container.crashed
backup.completed
backup.failed
security.login.success
security.login.failed
vault.credential.used
automation.started
automation.completed
automation.failed
ai.recommendation.created
ai.action.approval.required
connector.connected
connector.disconnected
plugin.installed
plugin.disabled
```

Event names should be clear, predictable, and stable.

---

## Severity Levels

Events should include severity when appropriate.

Recommended severities:

```text
debug
info
notice
warning
error
critical
emergency
```

Severity should describe operational importance, not emotional tone.

---

## Event Categories

Events may belong to categories such as:

* Asset
* Connector
* Security
* Automation
* AI
* Plugin
* System
* Telemetry
* Audit
* User
* Workflow
* Notification

Categories help filtering, routing, dashboards, and permissions.

---

## Event Sources

Events may come from:

* Connectors
* Plugins
* Agents
* Users
* Automations
* AI systems
* Scheduled jobs
* Internal services
* External webhooks

Every event must identify its source.

---

## Actors

An event should distinguish the source from the actor.

The source is the system that emitted the event.

The actor is the entity responsible for the action.

Examples of actors:

* User
* Connector
* Plugin
* Agent
* Automation
* AI
* API client
* System

This distinction is important for audit logging and security.

---

## Correlation

Related events should share a correlation ID.

Example:

```text
User requests Docker update
    ↓
automation.started
    ↓
vm.snapshot.created
    ↓
container.updated
    ↓
healthcheck.passed
    ↓
automation.completed
```

All events in the chain should share the same `correlation_id`.

This allows Sentinel to explain what happened as one story instead of scattered logs.

---

## Event Storage

Sentinel should store events for historical analysis.

Stored events support:

* Audit trails
* Troubleshooting
* Trend analysis
* AI reasoning
* Compliance
* Dashboards
* Incident review

Retention should be configurable.

Home users may keep limited history.

Enterprise users may require long-term retention.

---

## Event Routing

Events should be routable.

Examples:

```text
critical events → notifications
security events → audit log
telemetry events → metrics store
automation events → workflow history
AI events → review queue
asset events → knowledge engine
```

Routing rules should be configurable.

---

## Event Subscriptions

Systems should subscribe to event streams.

Examples:

* Dashboard subscribes to asset status events.
* Automation engine subscribes to trigger events.
* AI layer subscribes to high-signal events.
* Notification system subscribes to user-facing alerts.
* Audit system subscribes to security and privileged actions.

Subscriptions should support filtering by:

* Event type
* Asset
* Site
* Severity
* Source
* Category
* Organization
* User
* Time range

---

## Event Deduplication

Some systems generate repeated events.

Example:

```text
interface.down
interface.down
interface.down
interface.down
```

Sentinel should support deduplication and suppression to prevent alert fatigue.

Deduplication may consider:

* Event type
* Asset
* Source
* Severity
* Time window
* Event fingerprint

---

## Event Enrichment

Raw events may be enriched before storage or routing.

Example raw event:

```text
Interface xe-0/0/1 down
```

Enriched event:

```text
Core switch uplink to storage network is down.
Affected systems: TrueNAS, Immich, Jellyfin.
Severity: critical.
Maintenance window: none.
```

Enrichment may use:

* Asset relationships
* Knowledge graph
* Maintenance windows
* Ownership
* Dependencies
* Historical behavior
* Policies

---

## Event Normalization

Connectors may report events differently.

Sentinel should normalize events into a consistent model.

Example:

```text
Linux: service failed
Docker: container exited
Windows: service stopped unexpectedly
```

All may normalize to:

```text
service.health.changed
```

Normalization allows dashboards, automations, and AI systems to work across different technologies.

---

## Event-Driven Automation

Automations should be triggered by events.

Example:

```text
When backup.failed occurs:
1. Check backup target availability.
2. Check storage usage.
3. Create incident summary.
4. Notify owner.
5. Recommend next action.
```

Automations should remain inspectable, auditable, and reversible when possible.

---

## AI and Events

Artificial intelligence should consume events through Sentinel Core.

AI should not bypass the Event Engine.

AI may use events to:

* Summarize incidents
* Detect patterns
* Recommend actions
* Explain root causes
* Generate maintenance plans
* Create automations
* Identify abnormal behavior

AI-generated recommendations should also create events.

---

## Audit Events

Security-sensitive actions must generate audit events.

Examples:

* Login attempt
* Credential access
* Permission change
* Plugin installation
* Connector configuration change
* Command execution
* AI action approval
* Automation execution
* User creation
* Role change

Audit events should be protected from tampering whenever practical.

---

## Telemetry Events

High-frequency telemetry should be handled carefully.

Examples:

* CPU usage
* Memory usage
* Temperature
* Interface counters
* Optical power
* Disk latency

Telemetry may be stored differently from operational events.

Sentinel should avoid flooding the Event Engine with unnecessary high-frequency data.

---

## Event Reliability

The Event Engine should be reliable.

Requirements:

* Events should not be silently lost.
* Failed processing should be logged.
* Critical events should support durable storage.
* Subscribers should be isolated from each other.
* One failing subscriber should not break the event system.

---

## Ordering

Events should include timestamps.

Strict ordering across distributed systems may not always be possible.

Sentinel should preserve ordering where practical and use correlation IDs to reconstruct event chains.

---

## Permissions

Access to events should respect RBAC.

Examples:

* A user may see dashboard events but not credential events.
* A security administrator may see audit events.
* A plugin may only subscribe to events it has permission to access.
* AI may only access events allowed by policy.

---

## External Events

Sentinel should support external event ingestion.

Examples:

* Webhooks
* MQTT messages
* Syslog
* SNMP traps
* Prometheus alerts
* Home Assistant events
* CI/CD pipeline events
* Security tool alerts

External events should be authenticated, normalized, and tagged by source.

---

## Event Retention

Retention policies should be configurable.

Examples:

```text
Telemetry: 7 days
Operational events: 90 days
Audit events: 1 year
Critical incidents: indefinite
```

Enterprise deployments may require compliance-driven retention.

---

## Event Replay

Sentinel should eventually support event replay.

Event replay allows:

* Debugging automations
* Rebuilding knowledge state
* Testing AI reasoning
* Incident review
* Simulation
* Regression testing

Replay should never re-execute destructive actions unless explicitly requested in a safe test mode.

---

## Design Rules

1. Every meaningful change should become an event.
2. Events should be structured.
3. Events should be normalized.
4. Events should be auditable.
5. Events should be permission-controlled.
6. Events should support correlation.
7. Events should enrich knowledge.
8. Events should drive automation.
9. Events should inform AI.
10. Events should help users understand their environment.

---

## Long-Term Vision

The Event Engine should become Sentinel's nervous system.

It allows Sentinel to sense, understand, remember, explain, and act.

Without events, Sentinel is only a dashboard.

With events, Sentinel becomes aware.
