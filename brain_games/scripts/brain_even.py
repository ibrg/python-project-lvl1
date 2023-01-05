from brain_games.cli import (
    getPlayerAnswer,
    getPlayerName,
    getRandomeNumber,
    welcome,
    welcome_user,
    compareAnswers
)


def isEvenNumber(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def guestEvenNumber(player_name) -> str:    
    counter = 3

    while counter > 0:
        n = getRandomeNumber()
        print(f"Question: { n }")
        result = isEvenNumber(n)
        answer = getPlayerAnswer()

        if not  compareAnswers(result, answer, player_name):
            break
        counter -= 1
        
    else:
        print(f"Congratulations, { player_name }!")


def main():
    welcome()
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    player_name = getPlayerName()
    welcome_user(game_rule, player_name)
    guestEvenNumber(player_name)


if __name__ == '__main__':
    main()
