import prompt
import random
from brain_games.cli import getPlayerName


def getRandomeNumber() -> int:
    return random.randint(1, 100)


def isEvenNumber(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def getPlayerAnswer() -> str:
    asnwer = prompt.string('Your answer: ')
    return asnwer


def guestEvenNumber() -> str:
    name = getPlayerName()
    counter = 3

    while counter > 0:
        n = getRandomeNumber()
        print(f"Question: { n }")
        check_n = isEvenNumber(n)
        answer = str(getPlayerAnswer())

        if check_n == answer:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was '{check_n}'. \
             Let's try again, Bill!)")
            break

        counter -= 1
    print(f"Congratulations, { name } !")
