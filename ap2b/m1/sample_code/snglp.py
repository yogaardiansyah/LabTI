"""
Module for demonstrating single-process password hashing using hashlib.sha256
"""

import hashlib
import time

def hash_password(password):
    """
    Hash a password string using SHA-256 and return the hexadecimal digest.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def single_process_hashing(password_list):
    """
    Hash a list of passwords sequentially and print the time taken.
    
    Args:
        password_list (list): List of password strings to be hashed.

    Returns:
        list: List of hashed password strings.
    """
    results = []
    start = time.time()
    for pw in password_list:
        hashed = hash_password(pw)
        results.append(hashed)
    print("Single Processing Waktu:", time.time() - start)
    return results

if __name__ == "__main__":
    all_passwords = ["pass123", "hello", "admin", "test1", "admin#1234"] * 200000

    print("Mulai Single Processing")
    single_hashes = single_process_hashing(all_passwords)
