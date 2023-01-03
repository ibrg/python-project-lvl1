#!/usr/bin/env python3
import prompt


def getPlayerName():
    player_name = prompt.string('May I have your name? ')
    return player_name


def welcome_user():
    print('Welcome to the Brain Games!')
    print(f"Hello, { getPlayerName() }!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
