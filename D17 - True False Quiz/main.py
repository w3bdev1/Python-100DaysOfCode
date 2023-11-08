from questions import question_data
from question_model import Question

question_bank = [Question(q["text"], q["answer"]) for q in question_data]

q1 = question_bank[0]
print(q1.text, q1.answer)
