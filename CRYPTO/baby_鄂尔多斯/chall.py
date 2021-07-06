from Crypto.Util.number import *
from secret import p, q, w, flag

n = p * p * q * p
e = 65537

print(f'Hint: {w}')

x = p + 4324
y = p + 4325
z = q - 1

LHS = w*(x*z + y*z - x*y)
RHS = 4*x*y*z
assert LHS == RHS

c = pow(bytes_to_long(flag), e, n)
print(f'Ciphertext: {long_to_bytes(c).hex()}')