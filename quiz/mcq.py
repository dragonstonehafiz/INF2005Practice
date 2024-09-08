class MCQ:
    _question = ""
    """The question is just the string that will be printed when the question is up."""
    _options: list[tuple[str, any]]
    """Will contain a list of tuples with the first variable being the text for this option, and the second variable
    being what is returned when that option is chosen."""

    def __init__(self, question: str = "Default Question"):
        self._question = question
        self._options = []
        self._correctAnswer = None

    def add_option(self, option: tuple):
        """
        Adds a new option that will show up when the user answers a question.
        :param option: A new option that can be chosen in the MCQ
        """
        self._options.append(option)

    def clear_options(self):
        """
        Deletes all available options.
        """
        self._options.clear()

    def print_options(self):
        """
        Iterate through the options to print all of them.
        """
        print(self._question)
        for i in range(0, len(self._options)):
            curr_option = self._options[i]
            print(f"{i}: {curr_option[0]}")

    def pick_option(self):
        """
        Let the user pick from all available options. If the user enters something that isn't a number, return 'fail'
        """
        user_input = input("Please pick an option: ")
        if not user_input.isnumeric():
            return "fail"

        # Converts the user input into an index
        # This index will correspond with one of the questions
        user_input_int = int(user_input)
        if len(self._options) > user_input_int >= 0:
            return self._options[user_input_int][1]
        else:
            return "fail"

