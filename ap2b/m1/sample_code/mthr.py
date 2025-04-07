"""
Sample code for giving insight about Multi threading
"""
import os
import time
import threading
import requests

os.makedirs("mthr", exist_ok=True)

def fetch_and_save(image_url, idx):
    """
    Function for fetching the API and saving the image from the API
    """
    try:
        response = requests.get(image_url, timeout=10)
        img_url = response.json()["url"]
        print(f"[Thread {idx}] Fetched: {img_url}")

        img_data = requests.get(img_url, timeout=10).content
        with open(f"mthr/waifu_{idx}.jpg", "wb") as file:
            file.write(img_data)
        print(f"[Thread {idx}] Saved: waifu_{idx}.jpg")
    except requests.exceptions.RequestException as e:
        print(f"[Thread {idx}] Error: {e}")

url_list = ["https://api.waifu.pics/sfw/waifu"] * 5
start = time.time()

threads = []
for i, u in enumerate(url_list):
    thread = threading.Thread(target=fetch_and_save, args=(u, i))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Multithreaded waktu:", time.time() - start)
