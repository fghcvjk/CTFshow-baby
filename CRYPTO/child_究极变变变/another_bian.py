from Crypto.Util.number import *
import string
import hashlib
import itertools

def only_lowercase(x):
    return ''.join(c for c in x.lower() if c in string.ascii_letters)

def another_bian1(msg, keys):
    result = []
    for m, key in zip(msg, itertools.cycle(keys)):
        result.append(m.translate(key))
    return ''.join(result)

def another_bian2(msg, l):
    cols = []
    for i in range(l):
        cols.append(msg[i::l])
    return ''.join(cols)

def get_bian_alphabet(r):
    a = list(string.ascii_lowercase)
    for i in range(len(a) - 1, 0, -1):
        j = r.randrange(0, i)
        a[i], a[j] = a[j], a[i]
    return ''.join(a)

def get_keys(K, rng):
    keys = []
    for i in range(K):
        from_str = string.ascii_lowercase
        to_str = get_bian_alphabet(rng)
        keys.append(''.maketrans(from_str, to_str))
    return keys

def another_bian(msg, l, keys):
    return another_bian2(another_bian1(msg, keys), l)

class RNG:
    def __init__(self, seed):
        self.state = seed
        self.a = 4000052466248296793
        self.b = 2220333583933023749
        self.m = 7335897609223787041

    def next(self):
        self.state = ((self.state * self.a) + self.b) % self.m
        return self.state

    def randrange(self, low, high):
        assert high > low
        generate_range = high - low
        limit = generate_range * (self.m // generate_range)
        while True:
            res = self.next()
            if res <= limit:
                return (res % generate_range) + low

if __name__ == "__main__":
    with open("novel.txt", "r", encoding='utf-8') as f:
        msg = only_lowercase(f.read())
    with open("flag.txt", "r") as f:
        msg += only_lowercase(f.read())
    seed = bytes_to_long(hashlib.sha512(msg.encode()).digest())
    rng = RNG(seed)
    L = rng.randrange(3, 20)
    K = rng.randrange(3, 20)
    print(f"L = {L}")
    print(f"K = {K}")
    keys = get_keys(K, rng)
    with open("novel.bian.txt", "w") as f:
        f.write(another_bian(msg, L, keys))
