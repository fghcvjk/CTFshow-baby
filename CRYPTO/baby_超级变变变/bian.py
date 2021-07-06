from Crypto.Util.number import *
import string
import hashlib

def only_lowercase(x):
    return ''.join(c for c in x.lower() if c in string.ascii_letters)

def bian1(msg, key):
    from_str = string.ascii_lowercase
    to_str = key
    bian_trans = ''.maketrans(from_str, to_str)
    return msg.translate(bian_trans)

def bian2(msg, l):
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

def bian(msg, l, key):
    return bian2(bian1(msg, key), l)

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
    L = rng.randrange(3, 100)
    print(f"L = {L}")
    key = get_bian_alphabet(rng)
    with open("novel.bian.txt", "w") as f:
        f.write(bian(msg, L, key))
