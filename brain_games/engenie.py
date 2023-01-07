import prompt

COUNTER = 3


def compare_answers(answer, user_answer, player_name):
    answer = str(answer)
    user_answ = str(user_answer)

    if answer == user_answ:
        return 'Correct!'
    else:
        print(
            f"'{user_answ}' is wrong answer ;(. Correct answer was '{answer}'."
            f" Let's try again, { player_name }!)"
        )
        return False


def run(module):
    # Welcome messages
    print('Welcome to the Brain Games!')
    # Hello player
    player_name = prompt.string('May I have your name? ')
    print(f"Hello, { player_name }!")
    module.welcome()

    for _ in range(COUNTER):
        (question, answer) = module.game()
        print(question)
        player_answer = prompt.string('Your answer: ')
        check_answer = compare_answers(answer, player_answer, player_name)
        if not check_answer:
            break
        print(check_answer)
    else:
        print(f"Congratulations, { player_name }!")
