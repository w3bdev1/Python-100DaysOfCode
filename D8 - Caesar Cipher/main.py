import string

alphabets = [c for c in string.ascii_lowercase]

directive = input("Type 'e' to encrypt and 'd' to decrypt: ").strip().lower()
msg = input("Type your message: ").strip().lower()
shift = int(input("Shift number: ").strip())

def encrypt(text, shift_amount):
    new_message = ""
    for c in text:
        if c == ' ':
            new_message.append(c)
        else:
            new_alphabet_index = alphabets.index(c) + shift_amount
            new_message += alphabets[new_alphabet_index]
    print(f"Encrypted text: {new_message}")


if directive == 'e':
    encrypt(text=msg, shift_amount=shift)
elif directive == 'd':
    print("decrypting")
else:
    print("Invalid direction!")