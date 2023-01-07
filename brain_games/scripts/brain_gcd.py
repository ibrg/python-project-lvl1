from brain_games.cli import (
    compareAnswers,
    getPlayerAnswer,
    getPlayerName,
    getRandomeNumber,
    welcome,
    welcome_user,
)


def guesNod(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def game(player_name):
    counter = 3

    while counter > 0:
        a, b = getRandomeNumber(), getRandomeNumber()
        print(f"Question: { a } { b }")
        result = guesNod(a, b)
        answer = getPlayerAnswer()

        if not compareAnswers(result, answer, player_name):
            break

        counter -= 1
    else:
        print(f"Congratulations, { player_name }!")


def main():
    welcome()
    player_name = getPlayerName()
    game_rule = 'Find the greatest common divisor of given numbers.'
    welcome_user(game_rule, player_name)
    game(player_name)


if __name__ == '__main__':
    main()
