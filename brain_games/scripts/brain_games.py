#!/usr/bin/env python3
from brain_games.cli import welcome, welcome_user, getPlayerName


def main():
    welcome()
    welcome_user(player_name=getPlayerName())


if __name__ == '__main__':
    main()
