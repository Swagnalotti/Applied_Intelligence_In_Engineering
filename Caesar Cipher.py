#alphabet = ['a', 'b', ... , 'z']
alphabet = list("abcdefghijklmnopqrstuvwxyz")

def caesar_cipher(text, shift):
    encrypted = ""

    for char in text:
        if char == " ":
            encrypted = encrypted + " "
        else:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % 26
            encrypted = encrypted + alphabet[new_index]

    return encrypted


def caesar_decrypt(text, shift):
    decrypted = ""

    for char in text:
        if char == " ":
            decrypted = decrypted + " "
        else:
            old_index = alphabet.index(char)
            new_index = (old_index - shift) % 26
            decrypted = decrypted + alphabet[new_index]
    return decrypted

input_text = input("Enter text to encrypt: ")
shift = int(input("Enter your key: "))

encrypted_text = caesar_cipher(input_text.lower(), shift)
print(f"Encrypted text: {encrypted_text}")

for i in range(27):
    print(caesar_decrypt(encrypted_text, i))