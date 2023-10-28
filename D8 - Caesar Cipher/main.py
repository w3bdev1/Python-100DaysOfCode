import string

alphabets = [c for c in string.ascii_lowercase]

directive = input("Type 'e' to encrypt and 'd' to decrypt: ").strip().lower()
msg = input("Type your message: ").strip().lower()
shift = int(input("Shift number: ").strip())

def encrypt(text, shift_amount):
    new_message = ""
    for c in text:
        if c == ' ':
            new_message += ' '
        else:
            new_alphabet_index = alphabets.index(c) + shift_amount
            if new_alphabet_index > len(alphabets):
                new_alphabet_index = new_alphabet_index - len(alphabets)
            new_message += alphabets[new_alphabet_index]
    print(f"Encrypted text: {new_message}")

def decrypt(text, shift_amount):
    new_message = ""
    for c in text:
        if c == ' ':
            new_message += ' '
        else:
            new_alphabet_index = alphabets.index(c) - shift_amount
            if new_alphabet_index < 0:
                new_alphabet_index = len(alphabets) + new_alphabet_index
            new_message += alphabets[new_alphabet_index]
    print(f"Decrypted text: {new_message}")

if directive == 'e':
    encrypt(text=msg, shift_amount=shift)
elif directive == 'd':
    decrypt(text=msg, shift_amount=shift)
else:
    print("Invalid direction!")