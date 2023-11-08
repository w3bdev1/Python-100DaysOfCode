class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        q = self.question_list[self.question_number]
        user_answer = input(f"Q{self.question_number + 1}. {q.text} (True/False)? ")
        self.check_answer(user_answer, correct_answer=q.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"That's wrong. It was {correct_answer}.")

        print(f"SCORE: {self.score}/{self.question_number + 1}")
        print("\n")

    def still_has_question(self):
        return self.question_number < len(self.question_list)
