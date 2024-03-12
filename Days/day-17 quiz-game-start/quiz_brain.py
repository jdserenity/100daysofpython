class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def validate_response(self, answer, res):
        if res == answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("Sorry, you got it wrong.")

        if self.question_number == len(self.question_list):
            print("\nQuiz is over. Thanks for playing!")
            print(f"Your final score was {self.score}/{self.question_number}.")
            return

        print(f"Your score is now {self.score}/{self.question_number}.\n")

    def still_has_questions(self):
        return len(self.question_list) - self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            res = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
            if res not in ['true', 'false']:
                print('Please enter a valid response.')
            else:
                self.validate_response(current_question.answer, res)
                return
