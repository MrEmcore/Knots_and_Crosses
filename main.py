player_X = [' X |', ' X |', ' X ', ' X |', ' X |', ' X ', ' X |', ' X |', ' X ']
player_O = [' O |', ' O |', ' O ', ' O |', ' O |', ' O ', ' O |', ' O |', ' O ']

game_board = {
    'board_1': ' 1 |',
    'board_2': ' 2 |',
    'board_3': ' 3 ',
    'board_4': ' 4 |',
    'board_5': ' 5 |',
    'board_6': ' 6 ',
    'board_7': ' 7 |',
    'board_8': ' 8 |',
    'board_9': ' 9 '
}


def start_game():
    # print('Welcome to knots and crosses')
    # player_1 = input('Player 1: ')
    # player_2 = input('Player 2: ')
    # TODO: insert random to select which player goes first

    while True:
        print_game_board(game_board)
        player_1_choice(game_board)
        print_game_board(game_board)
        if not check_winner(game_board):
            break
        player_2_choice(game_board)
        if not check_winner(game_board):
            break


def print_game_board(game_board):
    print("\n")
    print(game_board.get('board_7') + game_board.get('board_8') + game_board.get('board_9'))
    print('---|---|---')
    print(game_board.get('board_4') + game_board.get('board_5') + game_board.get('board_6'))
    print('---|---|---')
    print(game_board.get('board_1') + game_board.get('board_2') + game_board.get('board_3'))
    print("\n")


def player_1_choice(game_board):
    player_choice = int(input("Please choose a space: "))
    if player_choice == 1:
        if game_board.get("board_1") == " 1 |":
            game_board.update({'board_1': player_X[0]})
        else:
            print("Space not available. Please choose another")
            player_1_choice(game_board)
    elif player_choice == 2:
        if game_board.get("board_2") == " 2 |":
            game_board.update({'board_2': player_X[1]})
        else:
            print("Space not available. Please choose another")
            player_1_choice(game_board)
    elif player_choice == 3:
        if game_board.get("board_3") == " 3 ":
            game_board.update({'board_3': player_X[2]})
        else:
            print("Space not available. Please choose another")
            player_1_choice(game_board)
    elif player_choice == 4:
        if game_board.get("board_4") == " 4 |":
            game_board.update({'board_4': player_X[3]})
        else:
            print("Space not available. Please choose another")
            player_1_choice(game_board)
    elif player_choice == 5:
        if game_board.get("board_5") == " 5 |":
            game_board.update({'board_5': player_X[4]})
        else:
            print("Space not available. Please choose another")
            player_1_choice(game_board)
    elif player_choice == 6:
        if game_board.get("board_6") == " 6 ":
            game_board.update({'board_6': player_X[5]})
        else:
            print("Space not available. Please choose another")
            player_1_choice(game_board)
    elif player_choice == 7:
        if game_board.get("board_7") == " 7 |":
            game_board.update({'board_7': player_X[6]})
        else:
            print("Space not available. Please choose another")
            player_1_choice(game_board)
    elif player_choice == 8:
        if game_board.get("board_8") == " 8 |":
            game_board.update({'board_8': player_X[7]})
        else:
            print("Space not available. Please choose another")
            player_1_choice(game_board)
    elif player_choice == 9:
        if game_board.get("board_9") == " 9 ":
            game_board.update({'board_9': player_X[8]})
        else:
            print("Space not available. Please choose another")
            player_1_choice(game_board)
    return player_choice


def player_2_choice(game_board):
    player_choice = int(input("Please choose a space: "))
    if player_choice == 1:
        if game_board.get("board_1") == " 1 |":
            game_board.update({'board_1': player_O[0]})
        else:
            print("Space not available. Please choose another")
            player_2_choice(game_board)
    elif player_choice == 2:
        if game_board.get("board_2") == " 2 |":
            game_board.update({'board_2': player_O[1]})
        else:
            print("Space not available. Please choose another")
            player_2_choice(game_board)
    elif player_choice == 3:
        if game_board.get("board_3") == " 3 ":
            game_board.update({'board_3': player_O[2]})
        else:
            print("Space not available. Please choose another")
            player_2_choice(game_board)
    elif player_choice == 4:
        if game_board.get("board_4") == " 4 |":
            game_board.update({'board_4': player_O[3]})
        else:
            print("Space not available. Please choose another")
            player_2_choice(game_board)
    elif player_choice == 5:
        if game_board.get("board_5") == " 5 |":
            game_board.update({'board_5': player_O[4]})
        else:
            print("Space not available. Please choose another")
            player_2_choice(game_board)
    elif player_choice == 6:
        if game_board.get("board_6") == " 6 ":
            game_board.update({'board_6': player_O[5]})
        else:
            print("Space not available. Please choose another")
            player_2_choice(game_board)
    elif player_choice == 7:
        if game_board.get("board_7") == " 7 |":
            game_board.update({'board_7': player_O[6]})
        else:
            print("Space not available. Please choose another")
            player_2_choice(game_board)
    elif player_choice == 8:
        if game_board.get("board_8") == " 8 |":
            game_board.update({'board_8': player_O[7]})
        else:
            print("Space not available. Please choose another")
            player_2_choice(game_board)
    elif player_choice == 9:
        if game_board.get("board_9") == " 9 ":
            game_board.update({'board_9': player_O[8]})
        else:
            print("Space not available. Please choose another")
            player_2_choice(game_board)
    return player_choice


def check_winner(game_board):
    winner_x = [("X" in game_board.get("board_1" and "board_2" and "board_3")),
                ("X" in game_board.get("board_4" and "board_5" and "board_6")),
                ("X" in game_board.get("board_7" and "board_8" and "board_9")),
                ("X" in game_board.get("board_1" and "board_4" and "board_7")),
                ("X" in game_board.get("board_2" and "board_5" and "board_8")),
                ("X" in game_board.get("board_3" and "board_6" and "board_9")),
                ("X" in game_board.get("board_1" and "board_5" and "board_9")),
                ("X" in game_board.get("board_3" and "board_5" and "board_7"))]

    for checks in winner_x:
        if checks:
            print("Player X wins!!")
            return False
        else:
            return True

    winner_y = [("Y" in game_board.get("board_1" and "board_2" and "board_3")),
                ("Y" in game_board.get("board_4" and "board_5" and "board_6")),
                ("Y" in game_board.get("board_7" and "board_8" and "board_9")),
                ("Y" in game_board.get("board_1" and "board_4" and "board_7")),
                ("Y" in game_board.get("board_2" and "board_5" and "board_8")),
                ("Y" in game_board.get("board_3" and "board_6" and "board_9")),
                ("Y" in game_board.get("board_1" and "board_5" and "board_9")),
                ("Y" in game_board.get("board_3" and "board_5" and "board_7"))]

    for checks in winner_y:
        if checks:
            print("Player Y wins!!")
            return False
        else:
            return True


if __name__ == "__main__":
    start_game()
