# Connector SDK Specification

> Connectors are how Sentinel understands the world.

Version: 1.0 (Draft)

---

# Purpose

The Connector SDK defines the standard architecture for integrating external systems with Sentinel.

A connector is responsible for discovering, observing, and interacting with external infrastructure while translating vendor-specific behavior into Sentinel's universal Asset, Event, and Knowledge models.

The Connector SDK enables contributors to build integrations without modifying Sentinel Core.

---

# Philosophy

Sentinel should understand infrastructure—not vendors.

Every connector should normalize vendor-specific APIs, protocols, and terminology into a consistent model.

Whether connecting to a Linux server, a Fujitsu optical shelf, a Kubernetes cluster, or an ESP32, the rest of Sentinel should interact with the same Asset and Event models.

---

# Design Goals

The Connector SDK should be:

* Stable
* Secure
* Versioned
* Event-driven
* Observable
* Testable
* Language-friendly
* Easy to extend

The SDK should minimize boilerplate while encouraging best practices.

---

# Connector Responsibilities

A connector is responsible for:

* Discovering assets
* Updating asset metadata
* Reporting health
* Publishing events
* Collecting telemetry
* Executing supported actions
* Maintaining connection state
* Reporting capabilities
* Respecting Sentinel security policies

A connector should not contain business logic.

---

# Connector Architecture

```text
External System
        │
        ▼
Connector
        │
        ▼
Connector SDK
        │
        ▼
Sentinel API
        │
        ▼
Sentinel Core
```

Connectors communicate only through the SDK and public APIs.

---

# Connector Lifecycle

Every connector follows the same lifecycle.

```text
Install

↓

Configure

↓

Validate

↓

Connect

↓

Discover

↓

Observe

↓

Publish

↓

Operate

↓

Disconnect

↓

Remove
```

Lifecycle events should be observable and auditable.

---

# Discovery

Connectors should discover infrastructure automatically whenever possible.

Discovery may include:

* Assets
* Relationships
* Capabilities
* Metadata
* Health
* Services
* Inventory

Discovery should be repeatable and idempotent.

---

# Asset Registration

Every discovered object should be registered through the Asset Registry.

Examples:

Linux Host

Docker Container

Virtual Machine

Optical Shelf

Line Card

Power Supply

Interface

Storage Pool

Temperature Sensor

Assets should never bypass the Asset Model.

---

# Telemetry

Connectors may publish telemetry.

Examples:

CPU

Memory

Temperature

Optical Power

Fan Speed

Voltage

Power Consumption

Network Throughput

Disk Latency

Telemetry should be normalized whenever practical.

---

# Events

Connectors publish events rather than directly invoking subsystems.

Examples:

Asset Discovered

Asset Offline

Temperature Warning

Interface Down

Power Supply Failed

Configuration Changed

Firmware Updated

Events become part of Sentinel's Event Engine.

---

# Capabilities

Every connector declares its capabilities.

Examples:

Discovery

Monitoring

Remote Commands

Configuration

Firmware Updates

Terminal Access

Performance Metrics

Health Checks

Notifications

Capabilities determine available operations.

---

# Connection Types

Examples include:

SSH

WinRM

HTTPS

REST

GraphQL

gRPC

SNMP

IPMI

Redfish

MQTT

AMQP

Serial

USB

Bluetooth

Proprietary APIs

Future protocols should integrate without changing the SDK.

---

# Authentication

Credentials should always originate from the Vault.

Supported methods may include:

Username/Password

SSH Keys

Certificates

API Tokens

OAuth2

Kerberos

Local Authentication

Connectors should never permanently store credentials.

---

# Polling and Streaming

Connectors may support:

Scheduled polling

Event subscriptions

Webhooks

Persistent streams

Message queues

Hybrid models

The connector should choose the most appropriate mechanism.

---

# Health

Every connector should report:

Connection State

Latency

Version

Last Successful Communication

Authentication Status

Discovery Status

Health should be visible through the Observability Engine.

---

# Error Handling

Errors should be classified.

Examples:

Connection Failed

Authentication Failed

Rate Limited

Timeout

Unsupported Operation

Protocol Error

Errors should include meaningful diagnostic information.

---

# Rate Limiting

Connectors should respect target systems.

The SDK should support:

Maximum request rates

Concurrency limits

Backoff strategies

Retry policies

Sentinel should avoid overwhelming managed infrastructure.

---

# Actions

Connectors may expose actions.

Examples:

Restart Service

Reboot Device

Execute Command

Update Configuration

Refresh Inventory

Run Diagnostics

Actions should respect RBAC and the Policy Engine.

---

# Observability

The SDK should automatically expose:

Execution duration

Connection latency

Error rates

Discovery duration

Polling frequency

Resource usage

Connectors should be observable by default.

---

# Testing

Connector developers should receive:

Mock APIs

Asset simulators

Event simulators

Telemetry generators

Integration tests

Reference implementations

Testing should not require production infrastructure.

---

# Documentation

Every connector should include:

Overview

Supported Platforms

Authentication Requirements

Capabilities

Limitations

Examples

Configuration

Permissions

Troubleshooting

Documentation is part of the connector.

---

# Versioning

Connectors should follow semantic versioning.

Compatibility with Sentinel Core should be declared explicitly.

Breaking changes should be minimized.

---

# Security

Connectors operate under:

RBAC

Policy Engine

Vault

Organization Boundaries

Audit Logging

Least Privilege

No connector should bypass Sentinel Core security.

---

# Extensibility

Connector developers should be able to add:

Custom Asset Types

Telemetry Providers

Health Calculators

Action Providers

Configuration Schemas

Protocol Adapters

Future technologies should require new connectors—not changes to Sentinel Core.

---

# Design Rules

1. Normalize vendor-specific behavior.
2. Discover assets automatically.
3. Publish events.
4. Respect Sentinel security.
5. Remain observable.
6. Minimize boilerplate.
7. Never store secrets.
8. Keep connectors stateless where practical.
9. Use public SDK interfaces only.
10. Make connector development approachable.

---

# Long-Term Vision

The Connector SDK should become the primary mechanism through which Sentinel learns about infrastructure.

A contributor should be able to integrate virtually any technology—from enterprise storage arrays to industrial PLCs, amateur radio equipment, optical transport systems, IoT devices, or future technologies—without modifying Sentinel Core.

By providing a stable, well-documented SDK, Sentinel empowers the community to extend the platform while maintaining a consistent operational model across every supported technology.
