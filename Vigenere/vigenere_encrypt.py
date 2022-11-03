import string

main = string.ascii_lowercase


def conversion(plain_text, key):
    index = 0
    cipher_text = ""

    # convert into lower case
    plain_text = plain_text.lower()
    key = key.lower()

    for c in plain_text:
        if c in main:
            # to get the number corresponding to the alphabet for key
            alpha_key = ord(key[index]) - ord('a')

            # to get the number corresponding to the alphabet for plaintext
            alpha_text = ord(c) - ord('a')

            # implementing algo logic here
            encrypt_num = (alpha_text + alpha_key) % 26     # to get alphabet encrypted
            convert_unicode = encrypt_num + ord('a')    # to convert for unicode
            convert_to_string = chr(convert_unicode)
            encrypt = convert_to_string

            # adding into cipher text to get the encrypted message
            cipher_text += encrypt

            # for cyclic rotation in generating key from keyword
            index = (index + 1) % len(key)
        else:
            cipher_text += c

    print("plain text: ", plain_text)
    print("cipher text: ", cipher_text)


plain_text = input("Enter the message: ")
key = input("Enter the key: ")

# calling function
conversion(plain_text, key)