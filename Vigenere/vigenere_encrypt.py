import string

plaintext = "we are discovered save your self"
key = "deceptive"
cipher = ""

index = 10

for c in plaintext:
    if c in string.ascii_lowercase:
        offset = ord(key[index]) - ord('a')

        ord(c) - ord('a') + offset
        index = (index + 1) % len(key)
    else:
        # add if is not a letter
        cipher = cipher + c




