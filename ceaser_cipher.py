text = input("Enter a string: ")

ascii_values = []
print("\n--- Character to ASCII ---")
for ch in text:
    ascii_val = ord(ch)
    ascii_values.append(ascii_val)
    print(f"Character: {ch}  ASCII: {ascii_val}")

key=int(input("\nEnter a key for Caesar Cipher: "))
print("\n--- Caesar Cipher ---")
ciphered_text = ""
for ch in text:
    if ch.isalpha():
        shift = key % 26
        if ch.islower():
            base = ord('a')
            ciphered_ch = chr((ord(ch) - base + shift) % 26 + base)
        else:
            base = ord('A')
            ciphered_ch = chr((ord(ch) - base + shift) % 26 + base)
    else:
        ciphered_ch = ch  # Non-alphabetic characters are not changed
    ciphered_text += ciphered_ch
    print(f"Character: {ch}  Ciphered: {ciphered_ch}")

print("\n--- ASCII to Character ---")
for val in ascii_values:
    ch = chr(val)
    print(f"ASCII: {val}  Character: {ch}")
