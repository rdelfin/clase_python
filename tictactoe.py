def print_board(board_values):
    print(f"{board_values[0]}|{board_values[1]}|{board_values[2]}")
    print(f"-----")
    print(f"{board_values[3]}|{board_values[4]}|{board_values[5]}")
    print(f"-----")
    print(f"{board_values[6]}|{board_values[7]}|{board_values[8]}")

# 0|1|2
# -----
# 3|4|5
# -----
# 6|7|8


def board_won(board_values, player):
    # Horizontal wins
    if board_values[0] == player and board_values[1] == player and board_values[2] == player:
        return True
    if board_values[3] == player and board_values[4] == player and board_values[5] == player:
        return True
    if board_values[6] == player and board_values[7] == player and board_values[8] == player:
        return True
    
    # Vertical wins
    if board_values[0] == player and board_values[3] == player and board_values[6] == player:
        return True
    if board_values[1] == player and board_values[4] == player and board_values[7] == player:
        return True
    if board_values[2] == player and board_values[5] == player and board_values[8] == player:
        return True
    
    # Diagonals
    if board_values[0] == player and board_values[4] == player and board_values[8] == player:
        return True
    if board_values[6] == player and board_values[4] == player and board_values[2] == player:
        return True
    return False


values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
next_player = "x"

print_board(values)

for turn in range(9):
    new_position = int(input("Give me a position: "))
    if turn % 2 == 0:
        new_player = "x"
    else:
        new_player = "o"

    values[new_position] = new_player
    print_board(values)
    if board_won(values, new_player):
        print("Ganaste! :)")
        break