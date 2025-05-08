# Original string
text = "Hello  World"  # Note: \\ is a single backslash

def to_binary(n):
    return format(n, '08b')  # Converts to 8-bit binary (e.g., '01000001' for 'A')

print("Original String:", text)

print("\n--- AND Operation with 127 ---")
print("Char | ASCII | Binary      | 127     | AND Bin  | AND Char")
print("------------------------------------------------------------")
for char in text:
    original_ascii = ord(char)
    and_ascii = original_ascii & 127
    print(f"  {char}   |  {original_ascii:5} | {to_binary(original_ascii)} | {to_binary(127)} | {to_binary(and_ascii)} |   {chr(and_ascii)}")

print("\n--- XOR Operation with 127 ---")
print("Char | ASCII | Binary      | 127     | XOR Bin  | XOR Char")
print("------------------------------------------------------------")
for char in text:
    original_ascii = ord(char)
    xor_ascii = original_ascii ^ 127
    print(f"  {char}   |  {original_ascii:5} | {to_binary(original_ascii)} | {to_binary(127)} | {to_binary(xor_ascii)} |   {chr(xor_ascii)}")
