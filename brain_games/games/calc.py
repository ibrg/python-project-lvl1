from random import choice, randint


def get_random_operator() -> choice:
    return choice(['-', '+', '*'])


def get_sum(a: int, b: int, operator: str) -> str:
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b


def welcome():
    print('What is the result of the expression?')


def game():
    a, b = randint(1, 100), randint(1, 100)
    operator = get_random_operator()
    question = f"Question: { a } { operator } { b}"
    answer = get_sum(a, b, operator)
    return question, answer
