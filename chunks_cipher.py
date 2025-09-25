text=input("Enter a string: ")
chunk_size = int(input("Enter chunk size: "))

chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
print("\n--- Text Chunks ---")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
print("\n--- Character to ASCII ---")
ascii_values = []
for char in text:
    ascii_values.append(ord(char))
    print("\n--- ASCII Values ---")
for i, val in enumerate(ascii_values):
    print(f"Character: {text[i]}  ASCII: {val}")
ciphered_text = ""
print("\n--- Caesar Cipher ---")
key = int(input("Enter a key for Caesar Cipher: "))
for char in text:
    if char.isalpha():
        shift = key % 26
        if char.islower():
            base = ord('a')
            ciphered_char = chr((ord(char) - base + shift) % 26 + base)
        else:
            base = ord('A')
            ciphered_char = chr((ord(char) - base + shift) % 26 + base)
    else:
        ciphered_char = char  # Non-alphabetic characters are not changed
    ciphered_text += ciphered_char
    print(f"Character: {char}  Ciphered: {ciphered_char}")
print("\n--- Ciphered Text ---")
print(ciphered_text)