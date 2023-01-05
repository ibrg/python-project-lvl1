from brain_games.cli import (
    getPlayerAnswer,
    getPlayerName,
    getRandomeNumber,
    welcome,
    welcome_user,
)


def isEvenNumber(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def guestEvenNumber() -> str:
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    player_name = getPlayerName()
    welcome_user(game_rule, )

    counter = 3

    while counter > 0:
        n = getRandomeNumber()
        print(f"Question: { n }")
        result = isEvenNumber(n)
        answer = getPlayerAnswer()

        if result == answer:
            print('Correct!')
        else:
            print(
                f"{answer} is wrong answer ;(. Correct answer was '{result}'.\
                Let's try again, { player_name }!)"
            )
            break

        counter -= 1
    else:
        print(f"Congratulations, { player_name }!")


def main():
    welcome()
    guestEvenNumber()


if __name__ == '__main__':
    main()
