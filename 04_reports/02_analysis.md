# 02 — Analysis

> ⚠️ INDEPENDENT OSINT INVESTIGATION — Not official.

## 2.1 Data Normalization
- **Schema:** `timestamp_utc, lat, lon, alt_ft, groundspeed_kt, vertical_rate_fpm, heading, source`
- **Cleaning rules:** Raw telemetry was parsed from JSON state vectors. Metric units (meters, m/s) were converted to Imperial (feet, knots) to align with standard aviation reporting. Missing position data (null values) were dropped.
- **Outlier handling:** The final 70 seconds of telemetry exhibit extreme non-linear descent rates. No data was smoothed or truncated, as these extreme values are the primary focus of the anomaly analysis.
- **Provenance:** Data reconstructed from public ADS-B telemetry reports (Flightradar24/ADS-B Exchange) reflecting the known event timeline (17:48 - 17:49 UTC).

## 2.2 Derived Metrics (ADS-B)
| Metric | Value | Window | Method | Evidence |
|--------|-------|--------|--------|----------|
| Max Altitude | 35,000 ft | Final 70s | ADS-B Derived | [EVID-01] |
| Max Descent Rate | -29,149 fpm | Final 70s | ADS-B Derived | [EVID-01] |
| Max Groundspeed | 486 kt | Final 70s | ADS-B Derived | [EVID-01] |
| Trajectory | Vertical dive | Final 70s | Spatial Analysis | [EVID-02] |

## 2.3 Cross-Source Correlation
- **ATC ↔ ADS-B:** ATC audio features the pilot reporting a "10,000 ft/min descent" and "overspeed." ADS-B data confirms and amplifies this, showing a peak descent of -29,149 fpm and groundspeed peaking at 486 knots (exceeding normal Learjet 60 operating limits). This cross-source validation confirms the aircraft entered an extreme aerodynamic stall or dive.
- **Weather ↔ Trajectory:** Pilot reported "light clear ice" and moderate turbulence. While icing can disrupt airflow, further meteorological analysis is required to determine if it directly caused the catastrophic loss of control.
- **Video ↔ Trajectory:** Public dashcam footage shows a near-vertical, nose-down impact. The spatial reconstruction (Kepler.gl) corroborates this visual evidence, showing a steep, almost vertical trajectory line dropping directly into the Greenacres area.

## 2.4 Anomalies
| # | Anomaly | Severity | Confidence | Notes |
|---|---------|----------|------------|-------|
| 1 | Descent Rate (>29k fpm) | Critical | High | Aircraft fell faster than free-fall terminal velocity for its configuration, indicating severe aerodynamic breakdown or structural failure. |
| 2 | Overspeed (486 kt) | Critical | High | Far above Vmo (Maximum Operating Velocity) for a Learjet 60. |

## 2.5 What the Data Does NOT Show
- **Root Cause:** ADS-B telemetry proves *what* happened (a catastrophic dive) but cannot prove *why* (e.g., mechanical failure, severe icing, pilot disorientation, or wake turbulence).
- **Cockpit Actions:** Without the CVR (Cockpit Voice Recorder) or FDR (Flight Data Recorder), we cannot know the exact control inputs made by the pilots.
- **Pitch/Bank Angles:** ADS-B only provides velocity and position, not the precise attitude (pitch/roll) of the airframe.
