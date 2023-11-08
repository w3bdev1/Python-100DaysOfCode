from questions import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(q["text"], q["answer"]) for q in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You completed the quiz!")
print(f"Final score: {quiz.score}/{quiz.question_number}")