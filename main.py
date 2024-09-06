from modules.VigenereCipher import VigenereCipher
from modules.CaesarCipher import CaesarCipher

vigenere = VigenereCipher()

decoded = vigenere.decode("KS ME HZ BBL KS ME MPOG AJ XSE JCSFLZSY", "RELATIONS")
print(f"decoded: {decoded}")

encoded = vigenere.encode("TO BE OR NOT TO BE THAT IS THE QUESTION", "RELATIONS")
print(f"encoded: {encoded}")

caesar = CaesarCipher()

decoded = caesar.encode("All your base are belong to us", 5)
print(f"decoded: {decoded}")

encoded = caesar.decode("Fqq dtzw gfxj fwj gjqtsl yt zx", 5)
print(f"encoded: {encoded}")

