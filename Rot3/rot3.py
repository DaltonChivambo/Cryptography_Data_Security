import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
rot = 3

def encrypt(message):
    m = ''
    for c in message:
        if c in alphabet:
            c_index = alphabet.index(c)
            m += alphabet[(c_index+rot) % len(alphabet)]
        else:
            m += c
    return m.upper()

def decrypt(message):
    m = ''
    for c in message:
        if c in alphabet:
            c_index = alphabet.index(c)
            m += alphabet[(c_index-rot) % len(alphabet)]
        else:
            m += c;
    return m.upper()

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
