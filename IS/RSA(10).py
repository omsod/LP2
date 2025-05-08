def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    return d + phi if d < 0 else d

def power_mod(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result

def encrypt(msg, e, n):
    return [power_mod(ord(char), e, n) for char in msg]

def decrypt(cipher, d, n):
    return ''.join([chr(power_mod(char, d, n)) for char in cipher])

# --- Main Program ---
# Step 1: Input
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

if not (is_prime(p) and is_prime(q)):
    print("Both numbers must be prime!")
    exit()

# Step 2: Compute n, phi, e, d
n = p * q
phi = (p - 1) * (q - 1)

# Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 3
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

d = mod_inverse(e, phi)

# Step 3: Show key info
print("\nRSA Parameters:")
print(f"n  = p × q = {p} × {q} = {n}")
print(f"phi(n) = ({p}-1)×({q}-1) = {phi}")
print(f"Public exponent e = {e}")
print(f"Private exponent d = {d}")
print(f"\n Public Key: ({e}, {n})")
print(f" Private Key: ({d}, {n})")

# Step 4: Message input
message = input("\nEnter message to encrypt: ")

# Step 5: Encrypt
encrypted_msg = encrypt(message, e, n)
print("\nEncrypted message:", encrypted_msg)

# Step 6: Decrypt
decrypted_msg = decrypt(encrypted_msg, d, n)
print("Decrypted message:", decrypted_msg)
