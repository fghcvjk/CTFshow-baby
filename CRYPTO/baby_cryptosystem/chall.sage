load("secret.sage")

print(f"Base field F_q = {F}")
print(f"Modulus of base field: {F.modulus()}")
print()
print(f"Modulus of Extension Field: {K}")
print()

pub, priv = keygen()
for i, f_i in enumerate(pub):
    print(f"f_{i}: {f_i}")
print()

L1, L2, h_inv = priv
print(f"A_1: {list(L1[0])}")
print(f"b_1: {L1[1]}")
print()
print(f"A_2: {list(L2[0])}")
print(f"b_2: {L2[1]}")
print()

def byte2FF(b):
    return sum(int(bit) * alpha^i for i, bit in enumerate(bin(b)[2:].zfill(8)[::-1]))

def bytes2VV(b):
    assert len(b) <= n
    b += b"\0" * (n - len(b))
    return vector(F, [byte2FF(x) for x in b])

def xor(a, b):
    return bytes(x ^^ y for x, y in zip(a, b))

print("Have a check:")
print(decrypt(priv, bytes2VV(bytes([1] * n))))
print(encrypt(pub, bytes2VV(bytes([1] * n))))
print()

import secrets
k = secrets.token_bytes(len(FLAG))
print(f"Have an encryption: {encrypt(pub, bytes2VV(k))}")
print(f"Have a decryption: {decrypt(priv, bytes2VV(xor(k, FLAG)))}")
print()