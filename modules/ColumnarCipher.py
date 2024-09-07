def columnarCipherEncode(plaintext: str, key: str, order: str):
    key = key.upper()
    order = order.upper()
    # First we check if we need to add padding characters by finding the remainder of the total number of characters
    # divided by the total number of columns
    # We then get the characters we need to add from key_len - remainder
    remainder = len(plaintext) % len(key)
    padding_needed = len(key) - remainder
    for _ in range(0, padding_needed):
        plaintext += "X"

    # to do the columnar cipher we need to go from left to right using with all the letters
    # we'll go down to the next row when we reach the end of the key
    # we'll store each column as a list in a map, with the key being each letter in the key

    # initialize columns maps
    columns = {}
    for char in key:
        columns[char] = ""

    # we'll iterate through each char in the plaintext, at the same time iterating through each character in the key
    key_index = 0
    key_len = len(key)
    for char in plaintext:
        # this part gets the column we have to add the new character to
        key_letter = key[key_index]
        columns[key_letter] += char
        key_index = 0 if key_index+1 >= key_len else key_index+1

    # add the columns by iterating through the order list
    output = ""
    for char in order:
        output += columns[char]

    return output


def columnarCipherDecode(ciphertext: str, key: str, order: str):
    key = key.upper()
    order = order.upper()
    # first we find the number of characters per column
    key_len = len(key)
    column_len = int(len(ciphertext) / key_len)

    # create the map that will store each column, and then add each character
    columns = {}
    cipher_index = 0
    for char in order:
        columns[char] = ""
        for i in range(0, column_len):
            columns[char] += ciphertext[cipher_index]
            cipher_index += 1

    # to get the text back to the plain text form, we will have to start from the first row and move left to right
    #   K E Y
    #   0 1 2
    #   0 1 2
    #   0 1 2
    output = ""
    for i in range(0, column_len):
        for char in key:
            output += columns[char][i]

    return output



