import urllib.request
import time

url = "http://server-service:8080"

print(f"Client connecting to {url}...", flush=True)

try:
    with urllib.request.urlopen(url, timeout=5) as response:
        print(f"HTTP status: {response.status}", flush=True)
        print(f"Response: {response.read().decode()}", flush=True)

except Exception as e:
    print(f"Request failed: {e}", flush=True)

# Keep the client container alive
time.sleep(3600)