import prompt
from brain_games.cli import welcome, welcome_user, getRandomeNumber,\
    getPlayerName


def isEvenNumber(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def getPlayerAnswer() -> str:
    asnwer = prompt.string('Your answer: ')
    return asnwer


def guestEvenNumber() -> str:
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    player_name = getPlayerName()
    welcome_user(game_rule, )

    counter = 3

    while counter > 0:
        n = getRandomeNumber()
        print(f"Question: { n }")
        check_n = isEvenNumber(n)
        answer = str(getPlayerAnswer())

        if check_n == answer:
            print('Correct!')
        else:
            print(
                f"{answer} is wrong answer ;(. Correct answer was '{check_n}'.\
                Let's try again, Bill!)"
            )
            break

        counter -= 1
    print(f"Congratulations, { player_name }!")


def main():
    welcome()
    guestEvenNumber()


if __name__ == '__main__':
    main()
