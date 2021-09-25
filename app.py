from caesar_script import main as caesar
from helpers import exit_with_error
from vinegere_script import main as vinegere

if __name__ == '__main__':
    print('Welcome to THE decrypter!')
    print('Chose one of the available decrypter module to use.')
    print('1 - Caesar')
    print('2 - Vinegere')

    choice = input()

    if not choice:
        exit_with_error('No module was chosen!')

    if not choice.isdigit():
        exit_with_error('Module choice must be a digit!')

    choice = int(choice)

    if choice not in [1, 2]:
        exit_with_error('Unknown module choice!')

    if choice == 1:
        caesar()

    elif choice == 2:
        vinegere()
