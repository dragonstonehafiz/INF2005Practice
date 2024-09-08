import os
import sys

from quiz.mcq import MCQ
from questions.Question_DiffieHellman import Question_DiffieHellman
from questions.Question_DecodeColumnar import Question_DecodeColumnar

choose_qnd = MCQ("What type of Question would you like to do?")
choose_qnd.add_option(("Diffie Hellman Key Exchange", Question_DiffieHellman()))
choose_qnd.add_option(("Decoding Columnar Cipher", Question_DecodeColumnar()))
choose_qnd.add_option(("Quit", None))

chosen = None


while True:
    # Pick Question to generate
    while chosen is None:
        os.system('cls' if os.name == 'nt' else 'clear')
        choose_qnd.print_options()
        chosen = choose_qnd.pick_option()
        if chosen == "fail":
            input("Your choice was out of range. Press any key to try again.")
        elif chosen is None:
            sys.exit(0)

    # Answer Question
    chosen.mainloop()



