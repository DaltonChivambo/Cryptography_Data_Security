import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
rot = 3

def cipher(message, dir):
    m = ''
    for c in message:
        if c in alphabet:
            c_index = alphabet.index(c)
            m += alphabet[(c_index + (dir * rot)) % len(alphabet)]
        else:
            m += c
    return m.upper()

def encrypt(message):
    return cipher(message, 1)
def decrypt(message):
    return cipher(message, -1)

def main():
    command = sys.argv[1].lower()
    message = sys.argv[2].lower()

    if command == 'encrypt':
        print(encrypt(message))
    elif command == 'decrypt':
        print(decrypt(message))
    else:
        print(command + ' -> command not found')


if __name__ == '__main__':
    main()
