from modules.VigenereCipher import VigenereCipher
from modules.CaesarCipher import CaesarCipher
from modules.RailFenceCipher import railFenceEncode
from modules.ColumnarCipher import columnarCipherEncode

vigenere = VigenereCipher()

decoded = vigenere.decode("KS ME HZ BBL KS ME MPOG AJ XSE JCSFLZSY", "RELATIONS")
print(f"Vigenere Decoded: {decoded}")

encoded = vigenere.encode("TO BE OR NOT TO BE THAT IS THE QUESTION", "RELATIONS")
print(f"Vigenere Encoded: {encoded}")

caesar = CaesarCipher()

decoded = caesar.encode("All your base are belong to us", 5)
print(f"Caesar Decoded: {decoded}")

encoded = caesar.decode("Fqq dtzw gfxj fwj gjqtsl yt zx", 5)
print(f"Caesar Encoded: {encoded}")

encoded = railFenceEncode("HELLOBOB", 3)
print(f"Rail Fence Encode: {encoded}")

encoded = columnarCipherEncode("HELLOWORLD", "RED", "DER")
print(f"Columnar Cipher Encode: {encoded}")