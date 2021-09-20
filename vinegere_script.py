import os
import string
from collections import deque

UPPER_CASE_A_CHARACTER = 65
KEY_LENGTH = int(os.environ.get('KEY_LENGTH', 3))


def build_tabula_recta():
    tabula_recta = {}
    shift_alphabet = deque(list(string.ascii_uppercase))

    for key_letter in string.ascii_uppercase:

        for index, letter in enumerate(shift_alphabet):
            tabula_recta[f'{key_letter}{letter}'] = string.ascii_uppercase[index]

        shift_alphabet.rotate(-1)

    return tabula_recta


def exit_with_error(message=''):
    print(message)
    print('Exiting...')
    exit(1)


def validate_inputs():
    if not raw_ciphertext:
        exit_with_error('Missing ciphertext!')

    if not raw_key:
        exit_with_error('Missing key!')

    if len(raw_ciphertext) != KEY_LENGTH:
        exit_with_error(f'The ciphertext must have exactly {KEY_LENGTH} characters!')

    if len(raw_key) != KEY_LENGTH:
        exit_with_error(f'The key must have exactly {KEY_LENGTH} characters!')

    if any(char.isdigit() for char in raw_ciphertext):
        exit_with_error('All characters in the ciphertext must be letters!')

    if any(char.isdigit() for char in raw_key):
        exit_with_error('All characters in the key must be letters!')

    return raw_ciphertext.upper(), raw_key.upper()


def decrypt():
    pass


if __name__ == '__main__':
    raw_ciphertext = input('The ciphertext to be decrypted: ')
    raw_key = input('The key used in the encryption: ')

    ciphertext, key = validate_inputs()
    tabula_recta = build_tabula_recta()
    plaintext = ''

    for index in range(KEY_LENGTH):
        cipher_to_plain = f'{key[index]}{ciphertext[index]}'
        plaintext += tabula_recta[cipher_to_plain]

    print(f'Plaintext: {plaintext}')
