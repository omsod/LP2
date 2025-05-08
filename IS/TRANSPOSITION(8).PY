import math

# Encryption Function
def encrypt_message(msg, key):
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(msg):
            cipher[col] += msg[pointer]
            pointer += key
    return ''.join(cipher)

# Decryption Function
def decrypt_message(cipher, key):
    num_of_columns = math.ceil(len(cipher) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(cipher)

    plaintext = [''] * num_of_columns
    col = 0
    row = 0

    for symbol in cipher:
        plaintext[col] += symbol
        col += 1

        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)

# --- Main Program ---

# Take message and key as input
message = input("Enter the message to encrypt: ").replace(" ", "")  # optional: remove spaces
key = int(input("Enter the numeric key : "))

# Encryption
encrypted = encrypt_message(message, key)
print("\nEncrypted Message:", encrypted)

# Decryption
decrypted = decrypt_message(encrypted, key)
print("Decrypted Message:", decrypted)
