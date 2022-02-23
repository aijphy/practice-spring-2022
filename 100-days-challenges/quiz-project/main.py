import json
import requests

from question_model import Question
from quiz_brain import QuizBrain


class User:
    score = 0;

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "user1")

question_bank = []


def generate_question_list():
    print('setting up request for trivia questions')
    url = "https://opentdb.com/api.php"
    num = input("number of questions:")
    difficulty = input("difficult (easy, medium, hard):")
    headers = {}
    params = {
        'amount': num,
        'category': '18',
        'difficulty': difficulty,
        'type': 'boolean'
    }
    print('getting response, please hold...')
    response = requests.get(url, headers=headers, params=params)
    trivia_list = json.loads(response.text)

    for i in trivia_list['results']:
        question_bank.append(Question(i['question'],i['correct_answer']))



generate_question_list()

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print("You've complete the quiz")
print(f"Your final score was: {brain.score}/{brain.question_number}")
