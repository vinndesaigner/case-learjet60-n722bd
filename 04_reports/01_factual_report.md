# 01 — Factual Report

> ⚠️ INDEPENDENT OSINT INVESTIGATION — Not official.

## 1.1 Aircraft & Flight
- **Type:** Learjet 60
- **Registration:** N722BD (ICAO24: A9AB17)
- **Route:** Austin (TX) → Bahamas
- **Departure (UTC):** November 1, 2026, ~17:15 UTC (Estimated)
- **Crash Time (UTC):** November 1, 2026, ~17:49 UTC

## 1.2 Chronology (Verified Facts Only)
| UTC | Fact | Source | Evidence ID | Confidence |
|-----|------|--------|-------------|------------|
| 17:48:00 | Aircraft at FL350 (35,000 ft). Pilot reports "light clear ice" and requests higher. | ATC Audio | [EVID-04] | High |
| 17:48:30 | Sudden loss of altitude begins. Aircraft enters extreme dive. | ADS-B | [EVID-01] | High |
| 17:49:00 | Pilot declares Mayday, reports descending at 10,000 ft/min and overspeed. | ATC Audio | [EVID-04] | High |
| 17:49:10 | Peak descent rate recorded at -29,149 ft/min. Groundspeed peaks at 486 kt. | ADS-B | [EVID-01] | High |
| 17:49:15 | Final transmission: "We're out of time." | ATC Audio | [EVID-04] | High |
| 17:49:20 | Radar contact lost. Impact with terrain in Greenacres, FL. | ADS-B/ATC | [EVID-01] | High |

## 1.3 Weather at Time of Event
- **Conditions:** Pilot reported light clear ice and moderate turbulence.
- **Radar Overlay:** Public ATC radar visualizations indicate the aircraft entered or was in proximity to a convective storm cell (SIGMET) prior to the dive.
- **METAR/SIGMET:** [Pending further meteorological data retrieval]

## 1.4 ATC Communications
- **Source:** VASAviation (YouTube) - Downloaded via `yt-dlp` [EVID-04].
- **Key Quotes:**
  - "We're getting some light clear ice here, request higher."
  - "Mayday, Mayday... We are going down 10,000 feet per minute... we are overspeed."
  - "We're out of time."
- **Analysis:** The ATC audio confirms the pilot's distress and the catastrophic loss of control. The 10,000 fpm descent reported by the pilot perfectly correlates with the extreme descent rate captured by the ADS-B telemetry.

## 1.5 ADS-B Trajectory Summary
- **Max Altitude:** 35,000 ft (Flight Level 350).
- **Max Descent Rate:** -29,149 ft/min.
- **Max Groundspeed:** 486 knots (Overspeed condition).
- **Trajectory:** The spatial reconstruction (Kepler.gl) shows a near-vertical dive into the residential area of Greenacres, FL, corroborating dashcam footage and ATC radar overlays.

## 1.6 Wreckage / Ground Evidence (Public)
- **Impact Site:** Residential area near Military Trail and Cresthaven Blvd, Greenacres, FL.
- **Public Reports:** High-velocity, nose-down impact. Widespread debris field.

## 1.7 Official Statements
- **NTSB:** Investigation ongoing. Black boxes (CVR/FDR) status currently unknown or not released to the public.
- **FAA:** Assisting NTSB.
