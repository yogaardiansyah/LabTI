"""
Sample code for giving insight about single threading (serial)
"""
import time
import os
import requests

os.makedirs("nmthr", exist_ok=True)

urls = ["https://api.waifu.pics/sfw/waifu"] * 5

start = time.time()

for i, url in enumerate(urls):
    try:
        r = requests.get(url, timeout=10)
        img_url = r.json()["url"]
        print(f"[Serial {i}] Fetched: {img_url}")

        img_data = requests.get(img_url, timeout=10).content
        with open(f"nmthr/waifu_{i}.jpg", "wb") as f:
            f.write(img_data)
        print(f"[Serial {i}] Saved: waifu_{i}.jpg")
    except requests.exceptions.RequestException as e:
        print(f"[Serial {i}] Error: {e}")

print("Serial waktu:", time.time() - start)
