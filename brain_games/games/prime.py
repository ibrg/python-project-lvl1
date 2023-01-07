from random import randint


def is_prime(num: int) -> str:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def welcome():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def game():

    gues_num = randint(1, 100)
    question = f"Question: {gues_num}"
    answer = is_prime(gues_num)

    return question, answer
