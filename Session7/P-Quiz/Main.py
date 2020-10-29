from Questions import Question

quiz_prompt = [
    "How many weeks are in a year?\n(a) 50\n(b) 52\n(c) 48\n\n",
    "What is the sum of 293 and 564?\n(a) 857\n(b) 747\n(c) 956\n\n",
    "How many senses does a human have?\n(a) 4\n(b) 5\n(c) 6\n\n",
    "How many consonants are in the alphabet?\n(a) 20\n(b) 18\n(c) 21\n\n",
    "What is the tallest mountain the world?\n(a) Mount Everest\n(b) Makalu\n(c) K2\n\n"
]

questions = [
    Question(quiz_prompt[0], "b", False),
    Question(quiz_prompt[1], "a", True),
    Question(quiz_prompt[2], "b", False),
    Question(quiz_prompt[3], "c", True),
    Question(quiz_prompt[4], "a", False)
]

def run_quiz(questions):
    num_right = 0
    points = 0
    for question in questions:
        answer = input(f"\n\nQuestion {questions.index(question)+1}: {question.prompt}")
        if answer == question.answer:
            num_right = num_right + 1
            points = points + 10
            if question.is_hard == True:
                points = points * 2
    percentage = (num_right / len(questions)) * 100
    print(f"You got a {percentage}% on this quiz")
    print(f"You scored {points} points on the quiz!")
    print()
    
run_quiz(questions)

