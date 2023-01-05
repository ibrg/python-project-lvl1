#!/usr/bin/env python3
import prompt
import random


def getRandomeNumber() -> int:
    return random.randint(1, 100)


def getPlayerName():
    return prompt.string('May I have your name? ')


def getPlayerAnswer() -> str:
    return prompt.string('Your answer: ')


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user(game_rule: str = None, player_name: str = None) -> str:
    if player_name:
        print(f"Hello, { player_name }!")
    if game_rule:
        print(game_rule)


def compareAnswers(correct_answer, user_answer, player_name):
    if str(correct_answer) == str(user_answer):
        return 'Correct!'
    else:
        print(
            f"{str(user_answer)} is wrong answer ;(. Correct answer was '{str(correct_answer)}'."
            f" Let's try again, { player_name }!)"
        )
        return False
 