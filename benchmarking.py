# import matplotlib
import time 
import os 
from chacha20_python3 import yield_chacha_xor_stream

def benchmark():
    print('todo: compare encryption times against varying num_rounds, key lengths, plaintext lengths, etc')

def run_test(num_rounds, key, plaintext): 
    """
    Encrypt the plaintext using VChaCha with the specified number of rounds and key
    Logs and returns the time for encryption 
    """
    iv = os.urandom(8)
    start = time.perf_counter()
    
    # Generate keystream and encrypt
    keystream = b''.join(
        bytes([b]) for b in yield_chacha_xor_stream(key, iv, 0, num_rounds)
    )
    ciphertext = bytes([p ^ k for p, k in zip(plaintext, keystream[:len(plaintext)])])
    end = time.perf_counter()
    elapsed = end - start
    print(f"Rounds: {num_rounds}, Key len: {len(key)}, Plaintext len: {len(plaintext)}, Time: {elapsed:.6f}s")
    return elapsed

if __name__ == '__main__':
    benchmark()

