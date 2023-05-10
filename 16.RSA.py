import random

def generate_key_pair(p, q):
    # Generate n = p * q
    n = p * q
    
    # Compute the Euler totient function of n
    phi = (p - 1) * (q - 1)
    
    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    
    # Compute the modular multiplicative inverse d of e modulo phi
    d = modinv(e, phi)
    
    # Return the public key (n, e) and the private key (n, d)
    return ((n, e), (n, d))

def encrypt(plaintext, public_key):
    # Unpack the public key
    n, e = public_key
    
    # Convert the plaintext to an integer m
    m = bytes_to_int(plaintext)
    
    # Compute the ciphertext c = m^e mod n
    c = pow(m, e, n)
    
    # Convert the ciphertext to bytes
    ciphertext = int_to_bytes(c)
    
    # Return the ciphertext
    return ciphertext

def decrypt(ciphertext, private_key):
    # Unpack the private key
    n, d = private_key
    
    # Convert the ciphertext to an integer c
    c = bytes_to_int(ciphertext)
    
    # Compute the plaintext m = c^d mod n
    m = pow(c, d, n)
    
    # Convert the plaintext to bytes
    plaintext = int_to_bytes(m)
    
    # Return the plaintext
    return plaintext

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def bytes_to_int(bytes):
    return int.from_bytes(bytes, byteorder='big')

def int_to_bytes(n):
    return n.to_bytes((n.bit_length() + 7) // 8, byteorder='big')
# Generate a key pair with p = 11 and q = 13
public_key, private_key = generate_key_pair(11, 13)

# Encrypt a message with the public key
plaintext = b'Hello, World!'
ciphertext = encrypt(plaintext, public_key)

# Decrypt the ciphertext with the private key
decrypted_text = decrypt(ciphertext, private_key)

print('Original message:', plaintext)
print('Ciphertext:', ciphertext)
print('Decrypted text:', decrypted_text)


