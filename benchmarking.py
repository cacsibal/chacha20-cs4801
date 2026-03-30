import time 
import os 

cache_dir = os.path.join(os.getcwd(), '.benchmark_cache')
os.makedirs(cache_dir, exist_ok=True)
os.environ.setdefault('MPLCONFIGDIR', cache_dir)
os.environ.setdefault('XDG_CACHE_HOME', cache_dir)

import matplotlib
from vchacha import vchacha_encrypt

matplotlib.use('Agg')

def benchmark(): # run tests for various numbers of rounds and plaintext length, save results to CSV, run visualization
    num_rounds_list = [8, 12, 16, 20]
    plaintext_lengths = [64, 256, 1024, 4096, 16384]
    key = os.urandom(32)
    results = []
    for num_rounds in num_rounds_list:
        for pt_len in plaintext_lengths:
            plaintext = os.urandom(pt_len)
            elapsed = run_test(num_rounds, key, plaintext)
            results.append({
                'num_rounds': num_rounds,
                'plaintext_length': pt_len,
                'time': elapsed
            })

    with open('benchmark_results.csv', 'w') as f:
        f.write('num_rounds,plaintext_length,time\n')
        for r in results:
            f.write(f"{r['num_rounds']},{r['plaintext_length']},{r['time']}\n")

    visualize_results(results)

def visualize_results(results):
    import matplotlib.pyplot as plt
    num_rounds_set = sorted(set(r['num_rounds'] for r in results))
    plt.figure(figsize=(10,6))
    for num_rounds in num_rounds_set:
        pts = [r for r in results if r['num_rounds'] == num_rounds]
        pts = sorted(pts, key=lambda x: x['plaintext_length'])
        x = [p['plaintext_length'] for p in pts]
        y = [p['time'] for p in pts]
        plt.plot(x, y, marker='o', label=f'{num_rounds} rounds')
    plt.xlabel('Plaintext Length (bytes)')
    plt.ylabel('Encryption Time (seconds)')
    plt.title('VChaCha Encryption Time vs Plaintext Length')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('benchmark_plot.png')

def run_test(num_rounds, key, plaintext): # time the encryption for given parameters
    """
    Encrypt the plaintext using VChaCha with the specified number of rounds and key
    Logs and returns the time for encryption 
    """
    iv = os.urandom(8)
    start = time.perf_counter()
    
    # Encrypt only the plaintext length instead of consuming the infinite keystream generator.
    ciphertext = vchacha_encrypt(plaintext, key, iv, 0, num_rounds)
    end = time.perf_counter()
    elapsed = end - start
    print(f"Rounds: {num_rounds}, Key len: {len(key)}, Plaintext len: {len(plaintext)}, Time: {elapsed:.6f}s")
    return elapsed

if __name__ == '__main__':
    
    benchmark()
