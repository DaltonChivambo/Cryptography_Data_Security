import sys


def encrypt(message):
    return message

def decrypt(message):
    return message

def rot3():
    command = sys.argv[1].lower()
    message = sys.argv[2].lower()

    if command == 'encrypt':
        print(encrypt(message))
    elif command == 'decrypt':
        print(decrypt(message))
    else:
        print(command + '-> command not found')


if __name__ == '__main__':
    rot3()
