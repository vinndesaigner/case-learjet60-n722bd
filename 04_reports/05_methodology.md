# 05 — Methodology

> ⚠️ SIMULATED / INDEPENDENT OSINT INVESTIGATION — Not official.

## 5.1 Evidence Acquisition
- Tools: `curl`, `yt-dlp`, `ffmpeg`, browser devtools
- Preservation: Raw files → `01_evidence_raw/`, work in `02_working/`
- Integrity: `sha256sum` → `05_hashes/`
- Timestamp: All UTC, ISO-8601 format

## 5.2 Chain of Custody
See `00_admin/evidence_register.csv`.
Each file has: source, URL, capture time, SHA-256, type, reliability.

## 5.3 Analysis Tools
- Python: `pandas`, `pyModeS` / `traffic`, `matplotlib`
- GIS: QGIS / Kepler.gl
- Audio: `ffmpeg`, Audacity
- Metadata: `exiftool`

## 5.4 Reproducibility
- All queries and scripts are saved in `03_analysis/`
- Notebooks are versioned (e.g., `analysis_v1.ipynb`)
- Seeds / filters are documented

## 5.5 Peer Review Log
| Date | Reviewer | Notes | Resolution |
|------|----------|-------|------------|
|      |          |       |            |
