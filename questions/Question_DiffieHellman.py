from questions.BaseQuestion import BaseQuestion
import random

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
PRIMES_COUNT = len(PRIMES)
RANGE_MAX = 100
RANGE_MIN = 20

class Question_DiffieHellman(BaseQuestion):
    G: int
    p: int
    a: int
    b: int

    def __init__(self):
        self.generate()

    def generate(self):
        p = PRIMES[random.randint(0, PRIMES_COUNT - 1)]
        G = p
        a = p
        b = p
        while G == p:
            G = PRIMES[random.randint(0, PRIMES_COUNT-1)]
        while a == G or a == p:
            a = random.randint(RANGE_MIN, RANGE_MAX)
        while b == G or b == p or b == a:
            b = random.randint(RANGE_MIN, RANGE_MAX)

        self.p = p
        self.G = G
        self.a = a
        self.b = b

        A = (G ** a) % p
        self.ans = (A ** b) % p
        self.ans_query = "What is the secret key?: "

        self.wrong_message = f"You are incorrect. The correct answer is {self.ans}."

    def print(self):
        print("Alice and Bob are using the DiffieHellman Key Exchange to generate a shared secret key.")
        print("")
        print(f"Known Values:")
        print(f"modulus, p = {self.p},")
        print(f"generator, G = {self.G},")
        print(f"Alice's key, a = {self.a},")
        print(f"Bob's key, b = {self.b}")
        print("")

    def validate(self, ans: str):
        return ans.isnumeric()

    def check_ans(self, ans: str) -> bool:
        return int(ans) == self.ans

