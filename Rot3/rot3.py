import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
rot = 3

def encrypt(message):
    m = ''
    for c in message:
        c_index = alphabet.index(c)
        m += alphabet[c_index+rot]
    return m.upper()

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
        print(command + ' -> command not found')


if __name__ == '__main__':
    rot3()
