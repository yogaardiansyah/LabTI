"""
Module for demonstrating multi-process password hashing using hashlib.sha256
"""

import hashlib
import time
import multiprocessing

def hash_password(password):
    """
    Hash a password string using SHA-256 and return the hexadecimal digest.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def multi_process_hashing(password_list):
    """
    Hash a list of passwords in parallel using multiprocessing and print the time taken.
    
    Args:
        password_list (list): List of password strings to be hashed.

    Returns:
        list: List of hashed password strings.
    """
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(hash_password, password_list)
    print("Multi Processing Waktu:", time.time() - start)
    return results

if __name__ == "__main__":
    all_passwords = ["pass123", "hello", "admin", "test1", "admin#1234"] * 200000

    print("Mulai Multi Processing")
    multi_hashes = multi_process_hashing(all_passwords)
