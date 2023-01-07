from random import randint

from brain_games.cli import (
    compareAnswers,
    getPlayerAnswer,
    getPlayerName,
    welcome,
    welcome_user,
)


def game(player_name):

    counter = 3

    while counter > 0:
        lst = [x for x in range(1, 50)]
        start_index = randint(1, len(lst) % 10)
        progres_num = randint(1, 4)
        play_lst = lst[start_index::progres_num]
        index = randint(1, len(play_lst) - 1)
        hide_num = play_lst[index]
        play_lst[index] = '..'
        print("Question: ", end='')
        print(*play_lst)

        answer = getPlayerAnswer()
        check_answer = compareAnswers(hide_num, answer, player_name)
        if not check_answer:
            break
        print(check_answer)
        counter -= 1
    else:
        print(f"Congratulations, { player_name }!")


def main():
    welcome()
    game_rule = 'What number is missing in the progression?'
    player_name = getPlayerName()
    welcome_user(game_rule, player_name)
    game(player_name)


if __name__ == '__main__':
    main()
