#!/usr/bin/env python3
import prompt
import random


def getRandomeNumber() -> int:
    return random.randint(1, 100)


def getPlayerName():
    return prompt.string('May I have your name? ')


def getPlayerAnswer() -> str:
    asnwer = prompt.string('Your answer: ')
    return asnwer


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user(game_rule: str = None, player_name: str = None) -> str:
    if player_name:
        print(f"Hello, { player_name }!")
    if game_rule:
        print(game_rule)
