from random import randint


def welcome():
    print('Answer "yes" if number even otherwise answer "no".')


def is_even_number(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def game() -> list:
    n = randint(1, 100)
    question = f"Question: {n}"
    answer = is_even_number(n)

    return question, answer
