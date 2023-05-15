def mod_inverse(a, m):
    """
    Returns the modular multiplicative inverse of a modulo m, if it exists.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b):
    """
    Decrypts a ciphertext that was encrypted using the affine cipher with the given values of a and b.
    """
    plaintext = ""
    a_inverse = mod_inverse(a, 26)
    for c in ciphertext:
        if c.isalpha():
            c = c.upper()
            p = chr(((a_inverse * (ord(c) - 65 - b)) % 26) + 65)
            plaintext += p
        else:
            plaintext += c
    return plaintext

ciphertext = "KICUMZJBIQTIQCEIDMTDQAKIQFDC"
plaintext = affine_decrypt(ciphertext, 9, 22)
print(plaintext)
