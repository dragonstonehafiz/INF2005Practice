def diffieHellmanExchange(p: int, G: int, a: int, b: int):
    """
    :param p: modulus
    :param G: generator
    :param a: private key a
    :param b: private key a
    """
    # Calculate the public keys A, and B
    A = (G ** a) % p
    B = (G ** b) % p
    # Secret Key
    K1 = (B ** a) % p
    K2 = (A ** b) % p

    print(K1, K2)

