import os

POSSIBLE_SHIFTS = range(26)
UPPER_CASE_A_CHARACTER = 65


def exit_with_error(message=''):
    print(message)
    print('Exiting...')
    exit(1)


def validate_file():
    if not file_to_decrypt:
        exit_with_error('Missing file path! Usage: python caesar_brute_force_decrypter.py ./secret.txt')

    if not os.path.exists(file_to_decrypt):
        exit_with_error('Given file path does not exist!')

    with open(file_to_decrypt) as file:
        words = file.readline()

        if not words:
            exit_with_error("There's no key to be decrypted!")

        words = words.split()

        if not words:
            exit_with_error("There's no key to be decrypted!")

        word = words[0].replace('\n', '')

        if not word:
            exit_with_error("There's no key to be decrypted!")

        return word.upper()


def decrypt():
    chars = [ord(char) for char in word]
    shifted_words = {}

    print('Shift -> Key')
    for shift in POSSIBLE_SHIFTS:
        shifted_word = ''

        for char in chars:
            shifted_char = chr(((char - UPPER_CASE_A_CHARACTER - shift) % 26) + UPPER_CASE_A_CHARACTER)
            shifted_word += shifted_char

        print(f'{shift} -> {shifted_word}')

        shifted_words[shifted_word] = shift

    with open('./portuguese-words.txt') as file:
        for portuguese_word in file.readlines():
            portuguese_word = portuguese_word.replace('\n', '').upper()

            try:
                right_shift = shifted_words[portuguese_word]

            except KeyError:
                pass

            else:
                print(f'Found right shift to decrypt!')
                print(f'{word} is {portuguese_word} using the shift {right_shift}.')
                return

        exit_with_error('No word in the possible wordlist was found while shifting!')


if __name__ == '__main__':
    file_to_decrypt = input('Enter the file to decrypt(full path): ')

    word = validate_file()
    decrypt()

