import os
import string
from collections import deque
from itertools import product

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

    if any(char.isdigit() for char in raw_ciphertext):
        exit_with_error('All characters in the ciphertext must be letters!')

    return raw_ciphertext.upper()


def generate_possible_keys(cipher_length):
    possible_keys = []

    for first, second, third in product(string.ascii_uppercase, string.ascii_uppercase, string.ascii_uppercase):
        key = (f'{first}{second}{third}' * (cipher_length // KEY_LENGTH + 1))[:cipher_length]

        possible_keys.append(key)

    return possible_keys


def retrieve_plain_from_cipher(key, cipher_length):
    plain = ''

    for index in range(cipher_length):
        plain += tabula_recta[f'{key[index]}{ciphertext[index]}']

    return plain


def decrypt():
    cipher_length = len(ciphertext)
    possible_keys = generate_possible_keys(cipher_length)
    possible_ciphers = {}

    for key in possible_keys:
        possible_cipher = retrieve_plain_from_cipher(key, cipher_length)
        possible_ciphers[possible_cipher] = key

    with open('./src/portuguese-wordlist.txt') as file:
        for word in file.readlines():
            word = word.replace('\n', '').upper()

            try:
                right_key = possible_ciphers[word]
            except KeyError:
                continue
            else:
                print(f'The key to {ciphertext} is {right_key}, which decrypting results into {word}')


if __name__ == '__main__':
    raw_ciphertext = input('The ciphertext to be decrypted: ')

    ciphertext = validate_inputs()
    tabula_recta = build_tabula_recta()

    decrypt()
