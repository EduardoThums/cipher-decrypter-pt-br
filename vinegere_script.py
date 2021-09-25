import os
import string
from collections import deque
from itertools import product

from helpers import exit_with_error

KEY_LENGTH = int(os.environ.get('KEY_LENGTH', 3))

tabula_recta = {}
plain_combinations = {}


def validate_inputs(raw_ciphertext: str):
    global plain_combinations

    if not raw_ciphertext:
        exit_with_error('Missing ciphertext!')

    if any(char.isdigit() for char in raw_ciphertext):
        exit_with_error('All characters in the ciphertext must be letters!')

    if len(raw_ciphertext) < KEY_LENGTH:
        exit_with_error('The cipher must have at least 3 characters!')

    ciphertext = raw_ciphertext.upper()

    plain_combinations = {letter: [] for letter in ciphertext[:3]}

    return ciphertext


def build_tabula_recta():
    global tabula_recta

    shift_alphabet = deque(list(string.ascii_uppercase))

    for plain_letter in string.ascii_uppercase:

        for index, key_letter in enumerate(string.ascii_uppercase):
            cipher_letter = shift_alphabet[index]

            tabula_recta[f'{key_letter}{cipher_letter}'] = plain_letter

            try:
                plain_combinations[cipher_letter].append(f'{plain_letter}{key_letter}')

            except KeyError:
                continue

        shift_alphabet.rotate(-1)

    return tabula_recta


def decrypt(cipher):
    possible_keys = []
    cipher_length = len(cipher)

    for x, y, z in product(*plain_combinations.values()):
        raw_key = f'{x[1]}{y[1]}{z[1]}'
        # The key should be extended until it reaches the ciphertext length
        key = (raw_key * (cipher_length // KEY_LENGTH + 1))[:cipher_length]

        possible_keys.append(key)

    combinations = {}
    for key in possible_keys:
        plain = retrieve_plain_from_cipher(cipher, key, cipher_length)
        combinations[plain] = key

    correct_combinations = {}

    with open('./src/portuguese-wordlist.txt') as file:
        for word in file.read().splitlines():
            word = word.upper()

            try:
                correct_key = combinations[word]

                correct_combinations[word] = correct_key

                print(f'FOUND PLAINTEXT: {correct_key} -> {word}')

            except KeyError:
                continue

    wrong_combinations = [(p, k) for p, k in combinations.items() if p not in correct_combinations]

    with open('./src/vinegere.log', 'w+') as file:
        for plain, key in wrong_combinations:
            file.write(f'{key} -> {plain}\n')

    if wrong_combinations:
        print('Brute force attempts can be found at: ./src/vinegere.log')


def retrieve_plain_from_cipher(cipher, key, cipher_length):
    plain = ''

    for index in range(cipher_length):
        plain += tabula_recta[f'{key[index]}{cipher[index]}']

    return plain


def main():
    raw_ciphertext = input('The ciphertext to be decrypted: ')

    ciphertext = validate_inputs(raw_ciphertext)
    build_tabula_recta()

    decrypt(ciphertext)


if __name__ == '__main__':
    main()
