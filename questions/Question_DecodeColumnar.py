from helper.Generators import genkey, genplaintext, genkeyorder
from modules.ColumnarCipher import columnarCipherEncode
from questions.BaseQuestion import BaseQuestion

class Question_DecodeColumnar(BaseQuestion):
    ciphertext: str
    key: str
    order: str

    def generate(self):
        self.ans = genplaintext()
        self.key = genkey()
        self.order = genkeyorder(self.key)
        self.ciphertext = columnarCipherEncode(self.ans, self.key, self.order)
        self.ans_query = f"(HINT {self.key} <-> {self.order}):"
        self.wrong_message = f"Incorrect, the decoded text is:\n{self.ans}"

    def print(self):
        print("The Columnar cipher was used to generate this cipher text:")
        print("")
        print(self.ciphertext)
        print(f"What is the decoded text?")

    def validate(self, ans: str):
        return True

    def check_ans(self, ans: str) -> bool:
        return ans == self.ans
