import numpy as np

from board import Board
from player import Player

mapping = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2]
           }


def player_input(player):
    """
    A function that can take in a player input and assign their marker as 'X' or 'O'.

    :return: marker
             position
    """
    while True:

        marker = input("Please assign your marker as 'X' or 'O': ")

        if marker:
            if marker.upper()[0] not in ['X', 'O']:
                print("Please give only 'X' or 'O'!!")
            else:
                if not player.check_marker(marker) and player.get_marker() in ['X', 'O']:
                    print("Please give your marker!")
                else:
                    break

    while True:
        try:
            position = int(input("Please assign your desired position (number 1-9)': "))
        except ValueError:
            print("Please provide an integer")
            continue

        if position in range(1, 10):
            break
        else:
            print("Please provide an integer in the range (1-9)")

    return marker.upper(), position


# marker, position = player_input()
# print("Player chose {} as a marker in position {}".format(marker,position))


def place_marker(board, marker, position):
    """
    A function that takes in the board list object, a marker ('X' or 'O'),
    and a desired position (number 1-9) and assigns it to the board.

    :param board: board object
    :param marker: marker that player chose
    :param position: position that player chose
    :return: board
    """
    x, y = mapping[position]

    board.board[x][y] = marker

    return board


# new_board = place_marker(new_board,marker,position)
# new_board.display_board()


def win_check(board, mark):
    """
    A function that takes in a board and a mark (X or O) and then checks to see if that mark has won

    :param board:
    :param mark:
    :return:
    """
    win = False

    if board.mark_occurrences(mark) >= 3:
        if np.all(board.board[0][:] == mark) or np.all(board.board[1][:] == mark) \
                or np.all(board.board[2][:] == mark) or np.all(board.board[:][0] == mark) \
                or np.all(board.board[:][1] == mark) or np.all(board.board[:][2] == mark) \
                or (np.all(board.board[0][0] == mark) and np.all(board.board[1][1] == mark) and np.all(board.board[2][2] == mark))\
                or (np.all(board.board[2][0] == mark) and np.all(board.board[1][1] == mark) and np.all(board.board[0][2] == mark)):
         win = True
    return win


# print(win_check(new_board,marker))

import random


def choose_first():
    """
    A function that uses the random module to randomly decide which player goes first.
    You may want to lookup random.randint()
    :return: Return a string of which player went first.
    """
    order = random.randint(1, 2)
    if order == 1:
        return 'player_1'
    else:
        return 'player_2'


def space_check(board, position):
    """
    A function that returns a boolean indicating whether a space on the board is freely available.
    :param board:
    :param position:
    :return: a boolean
    """
    free_space = True

    x, y = mapping[position]
    if board.board[x][y] != '':
        free_space = False

    return free_space


def full_board_check(board):
    """
    A function that checks if the board is full and returns a boolean value. True if full, False otherwise.
    :param board:
    :return: a boolean value
    """
    return np.all(np.isin(board.board, "", invert=True))


def player_choice(board, player):
    """
    a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6
    to check if it's a free position. If it is, then return the position for later use.
    :param board:
    :return: the position
    """

    marker, position = player_input(player)
    free_space = space_check(board, position)
    if free_space:
        return position


def replay():
    """
    A function that asks the player if they want to play again and returns a boolean True
    if they do want to play again.
    :return: the answer
    """
    while True:
        answer = input("Do you want to play again? (Y/N) ")
        if answer:
            if answer[0].upper() in ['Y', 'N']:
                break
            else:
                print("Please reply with 'Y' for Yes or 'N' for No")

    return True if answer == 'Y' else False


if __name__ == "__main__":
    print('Welcome to the Tic Tac Toe!')
    print('-------------------------------')

    while True:
        # Set the game up here
        player_1 = Player(input("Please 'player1' give your name: "))
        player_2 = Player(input("Please 'player2' give your name: "))
        board_game = Board()
        game_on = True

        # Choose randomly who plays first
        player = choose_first()

        # Print the message to the players
        if player == 'player_1':
            print("{} you can start playing first!".format(player_1.name))
        else:
            print("{} you can start playing first!".format(player_2.name))

        # Display Board
        board_game.display_board()

        if player == 'player_1':
            factor = 1
            marker, position = player_input(player_1)
            player_1.set_marker(marker)
            place_marker(board_game, marker, position)
        else:
            factor = -1
            marker, position = player_input(player_2)
            player_2.set_marker(marker)
            place_marker(board_game, marker, position)

        player = 'player_' + str(factor * 1 + int(player[-1]))

        if player == 'player_1':
            if marker == 'X':
                player_1.set_marker('O')
            else:
                player_1.set_marker('X')
        else:
            if marker == 'X':
                player_2.set_marker('O')
            else:
                player_2.set_marker('X')

        print("\nPlayer {} will play with marker {} .".format(player_1.name, player_1.get_marker()))
        print("Player {} will play with marker {} .\n".format(player_2.name, player_2.get_marker()))

        while game_on:

            # Print the message to the players
            if player == 'player_1':
                print("{} you can play now.".format(player_1.name))
            else:
                print("{} you can play now.".format(player_2.name))

            # Display Board
            print("Check the board")
            board_game.display_board()

            # Loop until player give a valid position
            while True:
                # Player input
                if player == 'player_1':
                    marker, position = player_input(player_1)
                else:
                    marker, position = player_input(player_2)
                # Check if the position is free
                if space_check(board_game, position):
                    # Place the marker into the position given
                    place_marker(board_game, marker, position)
                    break
                else:
                    print("This position is not free!. Choose a free position")



            # Check win
            if win_check(board_game, marker):
                if player == 'player_1':
                    print("Player {} wins!".format(player_1.name))
                else:
                    print("Player {} wins!".format(player_2.name))
                game_on = False

            if full_board_check(board_game):
                print("Game Draw!")
                game_on = False

            # Change the player
            factor = factor * (-1)
            player = 'player_' + str(factor * 1 + int(player[-1]))

        if not replay():
            break
