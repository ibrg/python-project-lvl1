from random import randint


def welcome():
    print('Find the greatest common divisor of given numbers.')


def guesNod(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def game():
    a, b = randint(1, 100), randint(1, 100)
    question = f"Question: { a } { b }"
    answer = guesNod(a, b)
    return question, answer
