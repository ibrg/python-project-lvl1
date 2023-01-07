from random import randint


LENGTH = 10


def welcome():
    print('What number is missing in the progression?')


def game():
    lst = [x for x in range(1, 50)]
    start_index = randint(1, 10)
    step = randint(1, 10)
    play_lst = lst[start_index::step]
    index = randint(1, len(play_lst) - 1)
    hide_num = play_lst[index]
    play_lst[index] = '..'
    question = f"Question: {' '.join(map(str, play_lst))}"

    return str(question), hide_num
