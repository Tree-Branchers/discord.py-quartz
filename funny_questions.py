from random import randint

funny_questions_list = ["fill", "with", "funny", "questions", "(the questions must be at the same index as their answer"]
funny_answers_list = ["fill", "with", "funny", "answers", "(the questions must be at the same index as their answer)"]


def get_questions():

    '''
        Here, we get random generated questions and their answers.
    '''

    global funny_questions_list
    global funny_answers_list

    questions_list = []

    for question in range(randint(50, 300)):  # must be in the questions and answers lists range. test with range(1, 3).

        questions_list.append(funny_questions_list[question]), questions_list.append(funny_answers_list[question])

    return questions_list


class FunnyQuestions:

    def __init__(self, questions_and_answers):
        self.questions = {
            "question":
            "answer",
        }
        self.q_and_a = questions_and_answers

    def fill_dictionary(self):

        '''
            This function, fills our dictionary :self.questions: with questions as keys, and answers as values.
        '''

        for index in range(len(self.q_and_a)):
            if index % 2 == 0:
                self.questions[self.q_and_a[index]] = self.q_and_a[index+1]

    def ask_question(self):

        '''
            Here, the user wants a funny question,
            so we generate random question from the available ones,
            and then we return the question and the answer.
        '''

        questions_list = [question for question in self.questions.keys()]
        question_index = randint(0, len(questions_list))
        question = questions_list[question_index]

        return question, self.questions[question]


funny_questions = FunnyQuestions(get_questions())
funny_questions.fill_dictionary()

''' And then, we need the user to click on a button or to ask a specific command '''
# EXAMPLE

__main__ = "!funq&a"
__name__ = input()

if __name__ == __main__:
    print(funny_questions.ask_question())
