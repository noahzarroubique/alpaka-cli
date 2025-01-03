import requests
import json
import subprocess
import time


# check if already run today
with open("last_run.json") as f:
    last_run = json.load(f)["last_run"]

if time.gmtime(time.time()).tm_yday == time.gmtime(last_run).tm_yday:
    print("Already run today")
    exit()


# check if device is connected
capture_output = subprocess.run(["adb.exe", "devices"], capture_output=True)

if "device" not in capture_output.stdout.decode().replace("devices", ""):
    print("No device connected")
    exit()

# OIDC Token Endpoint
TOKEN_ENDPOINT = "https://ubidentity.ubique.ch/connect/token"

# Refresh Token Parameters

with open("token.json") as f:
    refresh_token = json.load(f)["refresh_token"]

client_id = "ublinth-app"

data = {
    "client_id": client_id,
    "grant_type": "refresh_token",
    "refresh_token": refresh_token,
}

#"""
response = requests.post(TOKEN_ENDPOINT, data=data)
if response.status_code == 200:
    tokens = response.json()
    token = tokens["access_token"]
    if "refresh_token" in tokens:
        refresh_token = tokens["refresh_token"]
        with open("token.json", "w") as f:
            json.dump({"refresh_token": refresh_token}, f)
else:
    print("Failed to refresh token:", response.status_code, response.text)
#"""

adb_path = "adb.exe"

def download_and_install_apk(app_id: int, selected_channel: str):
    builds = requests.get("https://linth-ws.ubique.ch/v1/apps/" + str(app_id), headers={"Authorization": f"Bearer {token}"})

    channels = builds.json()["channels"]
    for channel in channels:
        if channel["category"] == selected_channel:
            main_build = channel["builds"][0]["id"]

    apk = requests.get("https://linth-ws.ubique.ch/v1/apps/apk/" + main_build, headers={"Authorization": f"Bearer {token}"})
    
    print("Downloaded APK")

    with open("app.apk", "wb") as f:
        f.write(apk.content)

    subprocess.run([adb_path, "install", "app.apk"], check=True)

    print("Installed APK")

    


with open("whitelist.json") as f:
    whitelist = json.load(f)

for app in whitelist["apps"]:
    print("Installing: ", app["name"])
    download_and_install_apk(app["id"], app["channel"])


# update last run
with open("last_run.json", "w") as f:
    last_run = time.time()
    json.dump({"last_run": last_run}, f)