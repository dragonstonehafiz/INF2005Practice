from abc import ABC, abstractmethod
import os

class BaseQuestion(ABC):
    ans: any
    correct_message: str = f"Good job, you got the right answer!"
    """This is the message that will be printed when the user give the right answer."""
    wrong_message: str = "default wrong"
    """This is the message that will be printed when the user gives the wrong answer."""
    ans_query: str = "default answer query"
    """This is the message that will be printed when the input function is called."""

    def __init__(self):
        self.generate()
        pass

    def mainloop(self):
        """
        This is the function that will be called when the user is being questions
        """
        done = False
        while not done:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print()
            ans = self.answer()
            valid = self.validate(ans)
            if not valid:
                continue

            correct = self.check_ans(ans)
            self.final(correct)
            done = True

    @abstractmethod
    def generate(self):
        """
        Generate all values for the question
        """
        pass

    @abstractmethod
    def print(self):
        """
        Print the question to the screen.
        """
        pass

    def answer(self) -> str:
        """
        Let the user answer the question
        """
        user_input = input(self.ans_query)
        return user_input

    @abstractmethod
    def validate(self, ans: str):
        """
        Check if the answer is valid
        :param ans: The answer the user submitted
        """
        pass

    @abstractmethod
    def check_ans(self, ans: str) -> bool:
        """
        Checks if the answer that the user submitted is correct
        :param ans: The answer the user submitted
        """
        pass

    def final(self, correct: bool):
        """
        Prints a message to the screen depending on whether the user got the question right or wrong.
        """
        if correct:
            print(self.correct_message)
        else:
            print(self.wrong_message)

        input("Press any key to continue: ")


