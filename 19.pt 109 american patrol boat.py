# Define the Playfair square
def create_square(key):
    # Remove duplicates from the key
    key = "".join(dict.fromkeys(key))

    # Fill the square with the remaining letters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    square = key
    for letter in alphabet:
        if letter not in key:
            square += letter
    return square

# Decrypt the Playfair code message
def decode_playfair(ciphertext, key):
    square = create_square(key)
    plaintext = ""

    # Split the ciphertext into pairs of letters
    pairs = []
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        if len(pair) == 2:
            pairs.append(pair)
        else:
            # Add a padding letter if the last pair has only one letter
            pairs.append(pair + "X")

    # Decrypt each pair of letters
    for pair in pairs:
        # Find the indices of the letters in the square
        row1 = square.index(pair[0]) // 5
        col1 = square.index(pair[0]) % 5
        row2 = square.index(pair[1]) // 5
        col2 = square.index(pair[1]) % 5

        # Decrypt the pair of letters
        if row1 == row2:
            # Same row
            plaintext += square[row1*5 + (col1-1)%5]
            plaintext += square[row2*5 + (col2-1)%5]
        elif col1 == col2:
            # Same column
            plaintext += square[((row1-1)%5)*5 + col1]
            plaintext += square[((row2-1)%5)*5 + col2]
        else:
            # Rectangle
            plaintext += square[row1*5 + col2]
            plaintext += square[row2*5 + col1]

    return plaintext

# Test the program with the given ciphertext and key
ciphertext = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ"
key = "PTBOAT"
plaintext = decode_playfair(ciphertext, key)
print(plaintext)
