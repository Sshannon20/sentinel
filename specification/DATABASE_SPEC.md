# Data Storage Specification

> Sentinel's architecture defines its data. Storage is an implementation detail.

Version: 1.0 (Draft)

---

# Purpose

The Data Storage Specification defines how Sentinel persists, retrieves, and manages information.

Rather than coupling Sentinel to a specific database technology, this specification defines logical data domains and storage responsibilities.

Implementations may evolve without changing Sentinel Core.

---

# Philosophy

Sentinel should depend on data models—not database engines.

Every subsystem owns its logical data.

Storage providers are replaceable.

Business logic should never depend on a specific SQL dialect or storage engine.

---

# Design Goals

The storage layer should be:

* Reliable
* Transactional where appropriate
* Observable
* Scalable
* Replaceable
* Secure
* Backup-friendly
* Migration-friendly

---

# Storage Domains

Sentinel organizes persistent data into logical domains.

Examples include:

* Organizations
* Users
* Roles
* Assets
* Relationships
* Knowledge
* Events
* Observations
* Workflows
* Automations
* Policies
* Vault Metadata
* Plugins
* Connectors
* Notifications
* Reports
* Configuration
* Audit Logs

Each domain has a clearly defined owner.

---

# Ownership

Subsystems own their data.

Examples:

Asset Registry

↓

Assets

Knowledge Engine

↓

Knowledge Graph

Event Engine

↓

Events

Observability Engine

↓

Observations

Automation Engine

↓

Execution History

The storage layer should not blur subsystem boundaries.

---

# Storage Abstraction

Core services should interact with storage through repositories or service interfaces.

Example:

```text
Knowledge Engine

↓

Knowledge Repository

↓

Storage Provider
```

No subsystem should query implementation-specific tables directly.

---

# Relationships

Sentinel should preserve relationships between data domains.

Examples:

Organization

↓

Assets

↓

Events

↓

Knowledge

↓

Workflows

Relationships are first-class data.

---

# Transactions

Operations affecting multiple domains should support transactional integrity where practical.

Examples:

Workflow execution

Policy updates

Role assignments

Asset registration

Credential rotation

Consistency should be prioritized.

---

# Search

Search should operate independently of storage implementation.

Capabilities may include:

* Full-text search
* Semantic search
* Asset search
* Event search
* Knowledge search
* Workflow search

Search indexes should be rebuildable.

---

# Historical Data

Historical records should be preserved according to retention policies.

Examples:

Events

Audit Logs

Observations

Workflow History

Automation History

Knowledge History

History enables trend analysis and incident investigation.

---

# Time-Series Data

High-frequency telemetry should be stored separately from operational metadata where practical.

Examples:

CPU

Memory

Temperature

Network Throughput

Power Consumption

Optical Levels

Time-series optimization should remain an implementation detail.

---

# Configuration

Configuration should be versioned.

Examples:

Connector configuration

Plugin settings

Workspace layouts

Policies

Organization settings

Configuration changes should generate audit events.

---

# Backup

Storage should support:

* Online backup
* Offline backup
* Incremental backup
* Point-in-time recovery
* Verification
* Restore testing

Backups should be automatable.

---

# Migration

Sentinel should support schema evolution.

Requirements:

* Versioned migrations
* Rollback where practical
* Validation
* Upgrade safety

Storage migrations should be repeatable.

---

# Multi-Tenancy

Organizations should remain logically isolated.

Storage implementations should support:

* Single organization
* Multiple organizations
* Hosted deployments
* MSP deployments

Isolation should not depend solely on the application layer.

---

# Encryption

Sensitive data should be protected.

Examples:

* Vault metadata
* User information
* API tokens
* Session data
* Configuration secrets

Encryption requirements should align with the Security Architecture.

---

# Audit

Every storage operation affecting security-sensitive data should be auditable.

Examples:

Create

Update

Delete

Restore

Migration

Import

Export

Audit history should be immutable where practical.

---

# Scalability

The storage architecture should support:

* Home deployments
* Small businesses
* Enterprise environments
* Large-scale multi-site installations

Scaling strategies should remain independent of storage technology.

---

# Extensibility

Plugins may define additional data models.

Requirements:

* Versioning
* Validation
* Isolation
* Backup support
* Migration support

Plugin data should integrate with Sentinel's lifecycle.

---

# Design Rules

1. Data models define storage.
2. Storage implementations remain replaceable.
3. Every subsystem owns its data.
4. Relationships are first-class.
5. Historical data is valuable.
6. Transactions protect consistency.
7. Search is independent of storage.
8. Backups are mandatory.
9. Migrations are versioned.
10. Storage should scale with Sentinel.

---

# Long-Term Vision

The storage layer should provide a durable foundation for Sentinel without constraining future evolution.

By separating logical data models from physical storage technologies, Sentinel remains adaptable as new databases, storage engines, and deployment models emerge.

The architecture should outlive any particular implementation.
