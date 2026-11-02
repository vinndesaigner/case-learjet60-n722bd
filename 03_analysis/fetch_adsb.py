import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("OPENSKY_CLIENT_ID")
CLIENT_SECRET = os.getenv("OPENSKY_CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    print("[!] Error: OAuth2 credentials not found in .env file.")
    exit(1)

# 1. Minta Token Akses
token_url = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
token_data = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET
}

print("[*] Requesting OAuth2 token...")
token_res = requests.post(token_url, data=token_data)

if token_res.status_code != 200:
    print(f"[!] Gagal dapet token. Status: {token_res.status_code}")
    print(token_res.text)
    exit(1)

access_token = token_res.json().get("access_token")
print("[+] Token didapat!")

# 2. Tarik Data
ICAO24 = 'a1b2c3' # <--- GANTI INI PAKE HEX ASLI N722BD KALO UDAH DAPET
START_TIME = 1762016400
END_TIME = 1762020000

url = f"https://opensky-network.org/api/flights/aircraft?icao24={ICAO24}&begin={START_TIME}&end={END_TIME}"
headers = {"Authorization": f"Bearer {access_token}"}

print(f"[*] Fetching ADS-B data for {ICAO24}...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    out_file = "../01_evidence_raw/adsb/raw_opensky_N722BD.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"[+] Success! Data disimpen di {out_file}")
else:
    print(f"[!] Gagal. Status: {response.status_code}")
    print(response.text)
