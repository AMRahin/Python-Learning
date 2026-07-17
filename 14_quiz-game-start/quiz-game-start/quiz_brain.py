


class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        self.current_question=self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q{self.question_number}.{self.current_question.text}True/False?")
        self.check_answer(user_answer,self.current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!")
            print(f"The correct answer was {self.current_question.answer}")
            self.score+=1
            print(f"Score:{self.score}/{self.question_number}")
        else:
            print("You chose the wrong answer!")
            print(f"The correct answer was {self.current_question.answer}")
            print(f"Score{self.score}/{self.question_number}")

