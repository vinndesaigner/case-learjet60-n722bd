# Learjet 60 (N722BD) — Independent OSINT Investigation

> ⚠️ **INDEPENDENT OSINT INVESTIGATION**
> This is a public, open-source reconstruction of the Learjet 60 (N722BD) crash in Greenacres, FL, on November 1, 2026. **This is not an official NTSB report.** No access to CVR/FDR was available.

## 📌 Case Summary
On November 1, 2026, a Learjet 60 (Registration: N722BD) crashed into a residential area in Greenacres, Florida, while en route from Austin, TX to the Bahamas. All 9 occupants tragically lost their lives. 

This investigation utilizes public **ADS-B telemetry**, **ATC communications**, and **meteorological data** to reconstruct the spatial and temporal dynamics of the aircraft's final 70 seconds.

## 🛠️ Methodology
This repository applies DFIR (Digital Forensics and Incident Response) principles to open-source aviation data:
1. **Acquisition & Preservation:** Data is timestamped in UTC and hashed (SHA-256) for integrity.
2. **Normalization:** Raw metric telemetry (meters/m/s) is converted to aviation standard (feet/knots).
3. **Spatial Reconstruction:** Trajectory is visualized using Kepler.gl to analyze descent rates and geographic impact.

## 📂 Repository Structure
- `00_admin/` — Case notes, evidence register, and chain of custody.
- `01_evidence_raw/` — Raw, untouched data (ADS-B JSON, ATC audio, etc.).
- `02_working/` — Normalized data (CSV).
- `03_analysis/` — Python scripts for data processing and reconstruction.
- `04_reports/` — The final forensic reports and visual evidence.
- `05_hashes/` — Cryptographic checksums for evidence integrity.

## 📊 Key Findings
- **Max Altitude:** 35,000 ft
- **Max Descent Rate:** -29,149 ft/min (Catastrophic dive)
- **Max Groundspeed:** 486 knots (Severe overspeed)
- **Trajectory:** Near-vertical dive into Greenacres, FL.

## 🔗 Read the Full Report
Navigate to [`04_reports/README.md`](04_reports/README.md) to read the detailed breakdown of the factual report, analysis, and limitations.

## 📊 Executive Summary
This independent OSINT investigation reconstructed the final 70 seconds of Learjet 60 (N722BD) before its crash in Greenacres, FL, on November 1, 2026. By correlating publicly available ADS-B telemetry, ATC audio recordings, and visual geolocation, the data reveals a catastrophic, near-vertical dive:

- **Max Altitude:** 35,000 ft
- **Peak Descent Rate:** -29,149 ft/min (far exceeding the pilot's reported 10,000 fpm)
- **Max Groundspeed:** 486 knots (Severe overspeed condition)
- **Time to Impact:** < 70 seconds

Visual verification via public dashcam footage (cross-referenced with Google Street View) confirms the aircraft fell vertically into the residential area, corroborating the spatial trajectory mapped in this repository.
