"""
Demonstrates a race condition when multiple threads write to a shared file
without synchronization. This can result in mixed or lost log entries.
"""

import threading
import time
from datetime import datetime

def write_log_race(thread_id):
    """
    Simulates writing to a log file from a specific thread without using locks.
    This is vulnerable to race conditions due to concurrent access.
    """
    for count in range(5):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        log_line = f"[{timestamp}] Thread-{thread_id} log entry {count}\n"
        with open("log_race_condition.txt", "a", encoding="utf-8") as f:
            f.write(log_line)
        time.sleep(0.01)

if __name__ == "__main__":
    threads = []

    for i in range(3):
        t = threading.Thread(target=write_log_race, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Log writing with race condition completed.")
