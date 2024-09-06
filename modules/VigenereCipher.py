class VigenereCipher:
    _letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    """In the Vigenere table, this is the column."""

    _vigenereTable: dict[str, str] = {}
    """Each key is a 'row' in the Vigenere Table."""
    def __init__(self):
        num_letter = len(self._letters)

        # To generate the Vigenere Table we will be going row by row, starting with A
        self._vigenereTable = {}
        for i in range(0, num_letter):
            curr_letter = self._letters[i]
            row = ""
            # Each row in the table starts with the letter of that row, i.e. row B will have its first letter be B
            # Knowing that, we will start another loop from THAT character and fill in the values up till Z
            for j in range(i, num_letter):
                row += self._letters[j]
            # To handle the remained of the characters after Z, we just need to start another loop from A to the row's starting letter
            for j in range(0, i):
                row += self._letters[j]

            self._vigenereTable[curr_letter] = row

    def __str__(self):
        output_str = ""
        for key, value in self._vigenereTable.items():
            output_str += f"{key}:{value}\n"
        return output_str

    def encode(self, plaintext: str, key: str):
        curr_key_index = 0
        key_len = len(key)
        # Change all characters to upper case since stored columns are upper case
        plaintext = plaintext.upper()
        key = key.upper()
        encoded = ""

        # for encoding, we iterate through each character in the plaintext
        for char in plaintext:
            # If the character is not a letter
            if char not in self._letters:
                encoded += char
                continue
            # to find the character that we need to change to, we find the position of the character in the letters list
            char_index = self._letters.index(char)

            # to get the row that we need to use, we just separately iterate through the key
            curr_key_char = key[curr_key_index]
            row_to_use = self._vigenereTable[curr_key_char]
            encoded += row_to_use[char_index]

            # This is just a single line that updates and wraps the curr key index
            curr_key_index = 0 if curr_key_index+1 >= key_len else curr_key_index+1

        return encoded

    def decode(self, ciphertext: str, key: str):
        curr_key_index = 0
        key_len = len(key)
        # Change all characters to upper case since stored columns are upper case
        ciphertext = ciphertext.upper()
        key = key.upper()
        decoded = ""

        # for encoding, we iterate through each character in the encoded text
        for char in ciphertext:
            # If the character is not a letter
            if char not in self._letters:
                decoded += char
                continue

            # to find the character that we changed from, we need a couple of things
            # 1. The row from the Vigenere Table we'll be using.
            # 2. The index of the decoded character from the identified row
            # 3. We then pass this index into letters list which is the columns

            # 1.
            curr_key_char = key[curr_key_index]
            row_to_use = self._vigenereTable[curr_key_char]
            # 2.
            char_index = row_to_use.index(char)
            # 3.
            decoded += self._letters[char_index]

            # This is just a single line that updates and wraps the curr key index
            curr_key_index = 0 if curr_key_index+1 >= key_len else curr_key_index+1

        return decoded
