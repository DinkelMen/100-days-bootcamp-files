from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
n = 0
for i in question_data:
    question_bank.append(Question(question_data[n]['text'], question_data[n]['answer']))
    n += 1

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f'You have completed the quiz!\nYour final score was: {quiz.score}/12 ')
