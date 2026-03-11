# ELK-ThreatForge 🔥

<div align="center">

![Elastic 8.x](https://img.shields.io/badge/Elastic-8.x-00B2A9?style=for-the-badge&logo=elastic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![EQL](https://img.shields.io/badge/Query-EQL%20%2F%20KQL-orange?style=for-the-badge)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge&logo=mitre)
![Python ML](https://img.shields.io/badge/Python-ML%20Anomaly-green?style=for-the-badge&logo=python)
![Zero-Trust](https://img.shields.io/badge/Zero--Trust%20SIEM-blueviolet?style=for-the-badge)

**Next-Gen Open-Source SIEM Arsenal | Elastic Stack 8.x + Autonomous Threat Hunting**

</div>

## Project Overview 

SIEM-ELK-ThreatForge is a fully containerized, production-based, open-source SIEM platform engineered to replicate enterprise-grade detection engineering used by Tier-1 MSSPs in the UAE and globally. Built on Elastic Stack 8.15+, the lab leverages **Elastic Agent Fleet management simulation**, **custom ingest pipelines with Painless scripting** for real-time log enrichment (geo-IP, user-agent parsing, MITRE tagging), and **Event Query Language (EQL)** + **Kibana Query Language (KQL)** for high-fidelity behavioral correlation far beyond basic rule-based alerting.

The architecture employs a single-node Elasticsearch cluster with **ILM policies**, **rollup indices** for long-term retention, and **machine-learning anomaly detection jobs** (simulated via hybrid Python + Elastic ML). Log ingestion is handled through **Filebeat + Winlogbeat + custom Elastic Agent policies**, forwarding Windows EVTX, Linux auditd/syslog, and network flows from multiple simulated endpoints.

Threat detection is powered by **15+ custom Sigma-to-EQL converted rules** mapped directly to MITRE ATT&CK v14 (T1003.001 Credential Dumping, T1021 Lateral Movement, T1486 Ransomware Impact, T1566 Phishing). The detection engine uses **sequence-based EQL** for multi-event correlation (e.g., “failed logon → LSASS access → SMB lateral movement within 60s”).

Anomaly detection is augmented with a **scikit-learn Isolation Forest + statistical baselining Python module** that ingests enriched logs via Elasticsearch Python client, flags off-hour brute-force, impossible travel, and entropy-based command-line anomalies automatically exporting STIX 2.1 IOCs and triggering Kibana alerts.

All components are orchestrated via Docker Compose (with persistent volumes and health checks), enabling one-command deployment. Simulated attack surface uses Atomic Red Team TTPs + custom PowerShell/Cobalt-Strike emulation scripts, producing 500–2000 events per simulation run. Professional incident response artifacts (timelines, kill-chain mapping, executive summaries) are auto-generated.

## Screenshots Gallery (Live SIEM in Action)

<div align="center">
  <img src="https://via.placeholder.com/800x450/00B2A9/FFFFFF?text=Kibana+Advanced+Dashboard+with+EQL+Sequences" width="48%" alt="Kibana Dashboard">
  <img src="https://via.placeholder.com/800x450/FF4D4D/FFFFFF?text=Real-Time+MITRE+ATT%26CK+Alerts+Dashboard" width="48%" alt="Live Alerts">
  <br><br>
  <img src="https://via.placeholder.com/800x450/4A90E2/FFFFFF?text=EQL+Sequence+Detection+for+Lateral+Movement" width="48%" alt="EQL Hunting">
  <img src="https://via.placeholder.com/800x450/9B59B6/FFFFFF?text=Python+ML+Anomaly+Detection+Report" width="48%" alt="Python ML">
</div>

**Replace the 4 placeholder images above with your real screenshots** (see instructions below).

## Architecture (Modern Elastic 8.x Design)
```mermaid
graph TD
    A[Endpoints: Windows + Linux + Auditd] -->|Elastic Agent + Filebeat/Winlogbeat| B[Ingest Pipelines + Painless Enrichment]
    B --> C[Elasticsearch 8.x + ILM + Rollups]
    C --> D[Kibana 8.x + EQL/KQL + ML Jobs + Alerting Framework]
    D --> E[Custom Detection Rules + MITRE ATT&CK Mapping + Sigma]
    E --> F[Python ML Anomaly (Isolation Forest) + STIX IOC Export]
    F --> G[Automated Incident Reports + Threat Hunt Playbooks]
