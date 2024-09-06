class CaesarCipher:
    _letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, plaintext: str, shiftby: int):
        plaintext = plaintext.upper()
        len_letters = len(self._letters)
        # We use modulus because when the shiftby is at 26, it loops back to A
        toshift = shiftby % len_letters

        output = ""
        for char in plaintext:
            # If the character is not a letter
            if char not in self._letters:
                output += char
                continue

            char_index = self._letters.index(char)
            char_index += shiftby
            # We mod the character in case it goes over 26
            char_index = char_index % len_letters
            output += self._letters[char_index]

        return output

    def decode(self, ciphertext: str, shiftby: int):
        ciphertext = ciphertext.upper()
        len_letters = len(self._letters)
        # We use modulus because when the shiftby is at 26, it loops back to A
        toshift = shiftby % len_letters

        output = ""
        for char in ciphertext:
            # If the character is not a letter
            if char not in self._letters:
                output += char
                continue

            char_index = self._letters.index(char)
            char_index -= shiftby
            # We mod the character in case it goes below 0
            char_index = char_index % len_letters
            output += self._letters[char_index]

        return output

