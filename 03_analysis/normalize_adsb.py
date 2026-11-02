import json
import pandas as pd
import os
from datetime import datetime, timezone

input_file = "../01_evidence_raw/adsb/reconstructed_N722BD.json"
output_file = "../02_working/normalized_adsb.csv"

print("[*] Processing ADS-B Telemetry...")

with open(input_file, 'r') as f:
    data = json.load(f)

states = data.get('states', [])
normalized_data = []

for s in states:
    if s[5] is None or s[6] is None: continue
    
    dt = datetime.fromtimestamp(s[3], tz=timezone.utc)
    ts_utc = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    alt_ft = s[7] * 3.28084 if s[7] else 0
    gs_kt = s[9] * 1.94384 if s[9] else 0
    vs_fpm = s[11] * 196.85 if s[11] else 0
    
    normalized_data.append({
        "timestamp_utc": ts_utc,
        "lat": round(s[6], 5),
        "lon": round(s[5], 5),
        "alt_ft": round(alt_ft, 0),
        "groundspeed_kt": round(gs_kt, 0),
        "vertical_rate_fpm": round(vs_fpm, 0),
        "heading": s[10],
        "source": "ADS-B Reconstructed"
    })

df = pd.DataFrame(normalized_data)
os.makedirs(os.path.dirname(output_file), exist_ok=True)
df.to_csv(output_file, index=False)
print(f"[+] Sukses! Data bersih disimpan di {output_file}")
print(df.head())
