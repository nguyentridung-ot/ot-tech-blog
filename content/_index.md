---
title: "Industrial OT Systems, Bilingual Safety SOPs & Async B2B Storefront"
date: 2026-11-13T18:00:00+07:00
draft: false
tags: ["Industrial OT", "LOTO", "OSHA", "Async B2B", "Min-Fee Protocol", "Docker", "PostgreSQL", "Grafana"]
categories: ["Technical Authority Storefront"]
description: "The official technical storefront and B2B async portal of Nguyễn Trí Dũng. Showcasing containerized OT Analytics engines, bilingual LOTO SOPs with SHA-256 hash seals, and zero-cost static site architecture."
bookToc: true
---

# Nguyễn Trí Dũng | Industrial OT & Automation Specialist

Welcome to my **Technical Authority Storefront** and **Async-First B2B Engineering Portal**. 

I specialize in **Industrial Operational Technology (OT) Analytics**, **Containerized Data Pipelines (Docker, PostgreSQL, Grafana)**, and **Bilingual Safety & LOTO Standard Operating Procedures (OSHA 29 CFR 1910.147)** with cryptographic SHA-256 integrity verification.

Operating on a strict **100% Asynchronous (Async-First), Zero-Meeting Model**, this platform provides international B2B partners, engineering teams, and plant managers with transparent access to high-moat digital IP, open-source technical specifications, and remote subcontracting services.

> **🔒 NDA & Compliance Notice:** All database schemas, SQL DDLs, Docker compose configurations, LOTO procedure steps, and telemetry metrics across this portal are constructed strictly upon the **Standard Reference Model (`FAC_GLOBAL_01`)**. Zero proprietary logs, live plant keys, or confidential client data are exposed.

---

## 1. The 4 Technical Pillars (Core Architecture Hub)

This portal is structured around **4 core engineering pillars**, each representing a fully documented, production-ready technical asset:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        TECHNICAL AUTHORITY STOREFRONT HUB                              │
├──────────────────────────┬──────────────────────────┬──────────────────────────────────┤
│ PILLAR 1: OT ANALYTICS   │ PILLAR 2: LOTO SOPS SHA  │ PILLAR 3: MIN-FEE PROTOCOL       │
│ Containerized Telemetry  │ OSHA Bilingual Matrix    │ 0 VNĐ/Month Static Architecture  │
│ PostgreSQL + Grafana     │ SHA-256 Hash Seal        │ Hugo + GitHub Pages + Tally.so   │
├──────────────────────────┴──────────────────────────┴──────────────────────────────────┤
│ PILLAR 4: ASYNC OPERATING MANIFESTO — Zero-Meeting B2B Screening & Technical Handoff   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 📍 Pillar 1: Industrial OT Analytics Engine
* **Focus:** Containerized data pipeline architecture for downtime reduction, MTTR/MTBF metrics, and MOP V7 Technical Debt calculation.
* **Tech Stack:** Docker Compose, PostgreSQL 16 (Time-Series DDL & Materialized Views), Grafana Control Room Dashboards, Python 3.12 Ingestion Workers.
* **Key Article:** [Industrial OT Analytics Engine – Architecture & Implementation Guide]({{< relref "/docs/03-ot-analytics/industrial-ot-analytics-engine-v2" >}})
* **SMRP-BoK OPL Series:** [SMRP One-Point Lessons – Reliability & KPI Standards]({{< relref "/docs/01-smrp-bok" >}})

### 📍 Pillar 2: Bilingual Safety & LOTO SOPs Framework (SHA-256 Sealed)
* **Focus:** Production-grade Lockout/Tagout procedures compliant with OSHA 29 CFR 1910.147, featuring bilingual (English - Vietnamese) action matrices, STAR verification tests, and automated CMMS API integration.
* **Security Layer:** Cryptographic SHA-256 digital seals ensuring immutable document verification and preventing field version drift.
* **Key Article:** [Bilingual Safety & LOTO SOPs Showcase Index (SHA-256 Verified)]({{< relref "/docs/02-loto-standards/loto-sop-sha256-v3" >}})

### 📍 Pillar 3: The Min-Fee Protocol (0 VNĐ/Month Infrastructure)
* **Focus:** Architectural blueprint for building zero-maintenance, zero-cost technical web storefronts and automated B2B lead funnels.
* **Tech Stack:** Hugo SSG, Hugo Book Documentation Theme, GitHub Pages + Actions CI/CD, Tally.so, and LemonSqueezy API.
* **Key Article:** [The Min-Fee Protocol for Industrial Engineers]({{< relref "/posts/min-fee-protocol-zero-cost-v2" >}})

### 📍 Pillar 4: Async-First Operating Manifesto & Engagement Rules
* **Focus:** Operational guidelines explaining why we operate strictly on a 100% asynchronous, zero-live-meeting model to maximize engineering throughput and deliver audit-ready technical codebases.
* **Key Article:** [Why I Work 100% Asynchronously – A Guide for B2B Partners]({{< relref "/posts/operating-manifesto-async-v2" >}})

---

## 2. Featured Showcase: Electrical & Automation LOTO SOP Series

Below is the published **5-Part Electrical & Automation LOTO SOP Series**, fully formatted with JSON payloads for **SAP PM** and **IBM Maximo** API ingestion:

| SOP ID | Equipment / Target System | Primary Energy Sources | Cryptographic SHA-256 Checksum | CMMS Payload Status |
| :--- | :--- | :--- | :--- | :---: |
| **`LOTO-ELEC-01`** | **Variable Frequency Drive (VFD) & MCC** | 400VAC 3-Phase, DC Bus (750VDC) | `da79d4cb758467bc468c5de458c3ad50b2c7d873862ea8590752ce872f5e6a54` | `READY (SAP/Maximo)` |
| **`LOTO-ELEC-02`** | **Central PLC/SCADA & Servo Drives** | 230VAC Control, 24VDC, Servo 400V | `94cb8cf90e91b8be9ec7a167d9fbf52fe1571f1b170ff66cccdfc588cbda4b92` | `READY (SAP/Maximo)` |
| **`LOTO-ELEC-03`** | **Industrial Capacitor Bank & UPS** | 400VAC Mains, 690V Capacitor, 384VDC UPS | `29fc12270877043f8b61d690b24e82f1780742afdb5a96cd88915a40ceae0c6b` | `READY (SAP/Maximo)` |
| **`LOTO-ELEC-04`** | **Substation & 22kV MV Switchgear** | 22kV Medium Voltage, 400V Bus | `f41c364dd5e0dabbfd22411b02e8bdda37b445d878076700c130046d4eca4e12` | `READY (SAP/Maximo)` |
| **`LOTO-ELEC-05`** | **Electric Heating Elements & Oven** | 400VAC Power, PID 230V, Thermal (>200°C) | `df29de46e3270148391e29cedabce411a1d46404311adfbea2006aa86e61c2b3` | `READY (SAP/Maximo)` |

* Access the complete index and Python SHA-256 verification scripts in the [LOTO SOP Showcase Index]({{< relref "/docs/02-loto-standards/loto-sop-sha256-v3" >}}).

---

## 3. Operational Comparison: Synchronous vs. Async-First Engineering

To maintain maximum technical rigor, our B2B engagement model eliminates real-time meeting fatigue in favor of asynchronous, audit-ready deliverables:

| Operational Dimension | Traditional Synchronous Consulting | Our Async-First Engineering Model |
| :--- | :--- | :--- |
| **Communication Channel** | Live Zoom / Teams calls, phone meetings | Written Specs, Slack/Jira Tickets, GitHub Issues, Email |
| **Time-Zone Flexibility** | Limited (Requires overlapping hours) | **Global / Universal** (US, EU, APAC seamless execution) |
| **Documentation Quality** | Informal verbal promises, meeting minutes | **100% Version-Controlled Code & SHA-256 Sealed Specs** |
| **Engineering Throughput** | Interrupted by calendar friction | **Uninterrupted 1.5h Block Time & Automated CI/CD** |
| **Quality Control** | Subject to real-time verbal misstatements | **Peer-Reviewed & AI Co-pilot Audited Codebases** |

---

## 4. 4-Step B2B Async Engagement Workflow

Partnering with us on remote Industrial OT Data Pipelines, Custom LOTO Digital IP Licensing, or Subcontracting follows a transparent, 4-step workflow:

```
 [Step 1: Technical Screening]
  └── Submit project scope via Tally.so Screening Form below.
                                      │
                                      ▼
 [Step 2: Async Technical Assessment]
  └── Receive structured B2 English proposal & STAR scope analysis within 24–48h.
                                      │
                                      ▼
 [Step 3: Repository Setup & Milestones]
  └── Work tracking established via private GitHub Repo, Jira Board, or Shared Slack.
                                      │
                                      ▼
 [Step 4: SHA-256 Code Handoff & CI/CD]
  └── Final code handoff signed with Cryptographic SHA-256 Seals & automated tests.
```

---

<div id="tally-form-anchor" style="scroll-margin-top: 30px;"></div>

## 5. B2B Async Technical Screening Form

If you require **Remote Industrial OT Data Contracting**, **Custom PostgreSQL/Grafana Pipeline Engineering**, or **LOTO Digital IP Licensing**, submit your technical inquiry through our gatekeeper form below. 

*All inquiries are processed asynchronously within 24–48 hours.*

<iframe data-tally-src="https://tally.so/embed/M1DrPA?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1" loading="lazy" width="100%" height="1158" frameborder="0" marginheight="0" marginwidth="0" title="B2B Async Technical Screening Form"></iframe>
<script>var d=document,w="https://tally.so/widgets/embed.js",v=function(){"undefined"!=typeof Tally?Tally.loadEmbeds():d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach((function(e){e.src=e.dataset.tallySrc}))};if("undefined"!=typeof Tally)v();else if(d.querySelector('script[src="'+w+'"]')==null){var s=d.createElement("script");s.src=w,s.onload=v,s.onerror=v,d.body.appendChild(s);}</script>

---

*Powered by the Min-Fee Protocol | Hosted on GitHub Pages | Static Architecture by Hugo*
