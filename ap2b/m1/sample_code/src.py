"""
Demonstrates thread-safe logging using a threading.Lock to prevent
race conditions when writing to a shared file.
"""
import threading
import time
from datetime import datetime

log_lock = threading.Lock()

def write_log_safe(thread_id):
    """
    Thread-safe logging function with synchronized timestamp generation and file writing.
    """
    for count in range(5):
        with log_lock:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            log_line = f"[{timestamp}] Thread-{thread_id} log entry {count}\n"
            with open("log_safe.txt", "a", encoding="utf-8") as f:
                f.write(log_line)
        time.sleep(0.01)

if __name__ == "__main__":
    threads = []

    for i in range(3):
        t = threading.Thread(target=write_log_safe, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Fixed thread-safe log writing completed.")
