from vchacha import yield_chacha_xor_stream

num_bytes = 2 ** 10
k1 = b'a' * 32
chunk_size = 8

for num_rounds in range(8, 32 + 1, 2):
    ks = yield_chacha_xor_stream(k1, b'\0' * 8, num_rounds=num_rounds)
    sample = [next(ks) for _ in range(num_bytes)]
    ks_binary = ''.join(format(b, '08b') for b in sample)
    pct_zeroes = ks_binary.count('0') / len(ks_binary)

    chunks = [bytes(sample[i:i + chunk_size]).hex() for i in range(0, len(sample), chunk_size)]

    chunk_dict = {}
    for chunk in chunks:
        if chunk in chunk_dict:
            chunk_dict[chunk] += 1
        else:
            chunk_dict[chunk] = 1

    if(len(chunk_dict) != num_bytes / chunk_size):
        print(f'num_rounds: {num_rounds} pct_zeroes: {pct_zeroes}')
        print('{')
        for chunk, count in chunk_dict.items():
            print(f"  '{chunk[:16]}...{chunk[-16:]}': {count},")
        print('}\n')