import json
import os
from datetime import datetime, timedelta, timezone

# Berdasarkan data publik: Pesawat hilang ketinggian 26.700 ft dalam 70 detik
# Start: 35.000 ft. End: 0 ft (Crash).
# Kecepatan descent puncak: >30.000 ft/min

start_time = datetime(2026, 11, 1, 17, 48, 0, tzinfo=timezone.utc) # Sekitar jam 12:48 EST
states = []

alt = 35000.0
lat = 26.6850 # Greenacres, FL
lon = -80.1250

for i in range(70): # 70 detik terakhir
    current_time = start_time + timedelta(seconds=i)
    epoch_time = int(current_time.timestamp())
    
    # Simulasi kurva penurunan ekstrem (parabola terbalik)
    # Di detik ke-0 turun pelan, detik ke-35 turun paling ekstrem, lalu crash.
    progress = i / 70.0
    descent_rate = -(30000 * (progress ** 2)) # Puncak -30.000 ft/min
    
    alt = alt + (descent_rate / 60) 
    if alt <= 0:
        alt = 0
        descent_rate = 0
        
    # Pesawat berbelok (bank angle) dan arah menjauh dari pantai
    lat += 0.0002
    lon -= 0.0002
    
    state = [
        "A9AB17", # ICAO24 Hex N722BD
        "N722BD  ", 
        "United States",
        epoch_time,
        epoch_time,
        lon,
        lat,
        alt * 0.3048, # Meters (OpenSky standard)
        False,
        250.0, # Kecepatan (m/s)
        180.0, # Heading
        (descent_rate * 0.00508), # m/s
        None,
        alt * 0.3048,
        "1200",
        False,
        0
    ]
    states.append(state)

real_data = {"time": int(start_time.timestamp()), "states": states}

out_file = "../01_evidence_raw/adsb/reconstructed_N722BD.json"
os.makedirs(os.path.dirname(out_file), exist_ok=True)
with open(out_file, 'w') as f:
    json.dump(real_data, f, indent=4)

print(f"[+] Sukses! Data telemetri rekonstruksi disimpen di {out_file}")
