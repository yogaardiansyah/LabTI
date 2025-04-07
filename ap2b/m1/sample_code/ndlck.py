"""
Demonstrates safe locking order to avoid deadlocks.
Both threads acquire locks in the same order (log -> db),
preventing circular waiting.
"""

import threading
import time

log_lock = threading.Lock()
db_lock = threading.Lock()

def safe_service(name):
    """Thread-safe function that always acquires locks in the same order."""
    with log_lock:
        print(f"[{name}] Locked log")
        time.sleep(0.5)
        with db_lock:
            print(f"[{name}] Locked db")
        print(f"[{name}] Released db")
    print(f"[{name}] Released log")

def run_safe_simulation():
    """Runs threads with consistent locking order to prevent deadlock."""
    print("\n--- Running safe lock order scenario ---")
    a = threading.Thread(target=safe_service, args=("A",))
    b = threading.Thread(target=safe_service, args=("B",))

    a.start()
    b.start()

    a.join()
    b.join()

    print("Done safely")

if __name__ == "__main__":
    run_safe_simulation()
