from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Helper to create an 8-byte key
def get_des_key_from_string(key_str):
    key_bytes = key_str.encode('utf-8')
    if len(key_bytes) < 8:
        key_bytes += b' ' * (8 - len(key_bytes))  # pad with spaces
    return key_bytes[:8]

# Get input from user
message = input("Enter the message to encrypt: ")
key_str = input("Enter an 8-character key: ")

# Validate key
if len(key_str) != 8:
    print("Key must be exactly 8 characters!")
    exit()

# Convert to bytes
key = get_des_key_from_string(key_str)
data = message.encode('utf-8')

# Pad data to match block size
padded_data = pad(data, DES.block_size)

# Create DES cipher
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt
encrypted_data = cipher.encrypt(padded_data)
print("\nEncrypted (hex):", binascii.hexlify(encrypted_data).decode())

# Decrypt
decrypted_data = cipher.decrypt(encrypted_data)
unpadded_data = unpad(decrypted_data, DES.block_size)
print("Decrypted message:", unpadded_data.decode('utf-8'))
