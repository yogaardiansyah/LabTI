"""
Simulates a classic deadlock scenario using two threads and two shared resources (locks).
Thread A locks the log file then the database.
Thread B locks the database then the log file.
This can lead to a deadlock if both threads hold one lock and wait for the other.
"""

import threading
import time

log_lock = threading.Lock()
db_lock = threading.Lock()

def service_a():
    """Thread A: locks log first, then db."""
    with log_lock:
        print("[A] Locked log")
        time.sleep(0.5)
        with db_lock:
            print("[A] Locked db")
        print("[A] Released db")
    print("[A] Released log")

def service_b():
    """Thread B: locks db first, then log."""
    with db_lock:
        print("[B] Locked db")
        time.sleep(0.5)
        with log_lock:
            print("[B] Locked log")
        print("[B] Released log")
    print("[B] Released db")

def run_deadlock_simulation():
    """Runs threads that may lead to deadlock."""
    print("\n--- Running deadlock-prone scenario ---")
    a = threading.Thread(target=service_a)
    b = threading.Thread(target=service_b)

    a.start()
    b.start()

    a.join()
    b.join()

    print("Done (if not stuck in deadlock)")

if __name__ == "__main__":
    run_deadlock_simulation()
