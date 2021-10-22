class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number <= len(self.question_list) - 1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} Is it true or false? [True - False]: ')
        value = self.check_answer(user_answer, current_question.answer)
        score_and_boolean = [self.keep_score(), value]
        return score_and_boolean

    def check_answer(self, user_answer, correct_answer, value=True):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        elif user_answer.lower() == "quit":
            value = False

        else:
            print('That\'s wrong.')
        print(f'The correct answer was: {correct_answer}')
        return value

    def keep_score(self):
        answered_questions = self.question_number
        print(f'Your current score is {self.score}/{answered_questions}')
        print('\n')
        score_list = [self.score, answered_questions]
        return score_list

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number <= len(self.question_list) - 1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} Is it true or false? [True - False]: ')
        value = self.check_answer(user_answer, current_question.answer)
        score_and_boolean = [self.keep_score(), value]
        return score_and_boolean

    def check_answer(self, user_answer, correct_answer, value=True):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        elif user_answer.lower() == "quit":
            value = False

        else:
            print('That\'s wrong.')
        print(f'The correct answer was: {correct_answer}')
        return value

    def keep_score(self):
        answered_questions = self.question_number
        print(f'Your current score is {self.score}/{answered_questions}')
        print('\n')
        score_list = [self.score, answered_questions]
        return score_list

