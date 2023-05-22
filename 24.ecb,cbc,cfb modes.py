from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
def encrypt_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# CBC Mode
def encrypt_cbc(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def decrypt_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# CFB Mode
def encrypt_cfb(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_cfb(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Test ECB Mode
key_ecb = get_random_bytes(16)
plaintext = b'This is a plaintext for ECB mode.'
ciphertext_ecb = encrypt_ecb(plaintext, key_ecb)
decrypted_ecb = decrypt_ecb(ciphertext_ecb, key_ecb)

print("ECB Mode:")
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext_ecb)
print("Decrypted:", decrypted_ecb.decode())

# Test CBC Mode
key_cbc = get_random_bytes(16)
iv_cbc = get_random_bytes(AES.block_size)
plaintext = b'This is a plaintext for CBC mode.'
ciphertext_cbc = encrypt_cbc(plaintext, key_cbc, iv_cbc)
decrypted_cbc = decrypt_cbc(ciphertext_cbc, key_cbc, iv_cbc)

print("\nCBC Mode:")
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext_cbc)
print("Decrypted:", decrypted_cbc.decode())

# Test CFB Mode
key_cfb = get_random_bytes(16)
iv_cfb = get_random_bytes(AES.block_size)
plaintext = b'This is a plaintext for CFB mode.'
ciphertext_cfb = encrypt_cfb(plaintext, key_cfb, iv_cfb)
decrypted_cfb = decrypt_cfb(ciphertext_cfb, key_cfb, iv_cfb)

print("\nCFB Mode:")
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext_cfb)
print("Decrypted:", decrypted_cfb.decode())
