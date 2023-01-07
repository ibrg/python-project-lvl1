from brain_games.cli import (
    getPlayerAnswer,
    getPlayerName,
    getRandomeNumber,
    welcome,
    welcome_user,
    compareAnswers
)


def isPrime(num: int) -> str:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def game(player_name):
    counter = 3

    while counter > 0:
        gues_num = getRandomeNumber()
        print(f"Question: {gues_num}")
        answer = getPlayerAnswer()
        result = compareAnswers(isPrime(gues_num), answer, player_name)
        if not result:
            break
        print(result)

        counter -= 1
    else:
        print(f"Congratulations, { player_name }!")


def main():
    welcome()
    player_name = getPlayerName()
    game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    welcome_user(game_rule, player_name)
    game(player_name)
