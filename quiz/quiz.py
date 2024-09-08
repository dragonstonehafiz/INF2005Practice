from questions.BaseQuestion import BaseQuestion


class Quiz:
    _questions: list[BaseQuestion]
    _currQn: int

    _currState: int = -1

    def add_qns(self, new_qns: BaseQuestion):
        self._questions.append(new_qns)
