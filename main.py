ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(text, key):
    # used alphabet x 2 to encrypt
    result = ''
    text = text.lower()
    encrypt_rule = ALPHABET * 2
    for letter in text:
        if letter in ALPHABET:
            letter_index = ALPHABET.index(letter)
            result += encrypt_rule[letter_index + key]
        else:
            result += letter
    return result


def decrypt(text, key):
    # used revers alphabet x 2 to decrypt
    result = ''
    decrypt_rule = ALPHABET[::-1] * 2
    for letter in text:
        if letter in ALPHABET:
            letter_index = ALPHABET[::-1].index(letter)
            result += decrypt_rule[letter_index + key]
        else:
            result += letter
    return result


if __name__ == "__main__":
    print("""
        1. Press 1 to Encrypt text \n
        2. Press 2 to Decrypt text \n
        3. Press 3 to do both \n
        """)

    choice = input('Select option: ')

    if choice == '1':
        text_to = input('Entre your text: ')
        key = int(input('Enter key between 1 to 25: '))
        print(encrypt(text_to, key))

    elif choice == '2':
        text_to = input('Entre your text: ')
        key = int(input('Enter key between 1 to 25: '))
        print(decrypt(text_to, key))

    elif choice == '3':
        text_to = input('Entre your text: ')
        key = int(input('Enter key between 1 to 25: '))
        encrypt_text = encrypt(text_to, key)
        print('Encrypt text: ', encrypt_text)
        print('Decrypt text: ', decrypt(encrypt_text, key))
    else:
        print('Wrong option!')
