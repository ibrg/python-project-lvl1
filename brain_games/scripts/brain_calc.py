from random import choice
from brain_games.cli import \
    welcome,\
    welcome_user, \
    getPlayerName, \
    getRandomeNumber, \
    getPlayerAnswer


def getRandomOperator() -> choice:
    return choice(['-', '+', '*'])


def getSum(a: int, b: int, operator: str) -> str:
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b


def Task():
    game_rule = 'What is the result of the expression?'
    player_name = getPlayerName()
    welcome_user(game_rule, player_name)
    counter = 3

    while counter > 0:
        a, b = getRandomeNumber(), getRandomeNumber()
        operator = getRandomOperator()
        result = getSum(a, b, operator)
        print(f"Question: { a } { operator } {b}")
        answer = int(getPlayerAnswer())

        if result != answer:
            print(
                f"{answer}' is wrong answer ;(. Correct answer was { result }."
                f"Let's try again, Sam!"
            )
            break
        print('Correct!')
        counter -= 1
    else:
        print(f"Congratulations, { player_name }!")


def main():
    welcome()
    Task()


if __name__ == '__main__':
    main()
