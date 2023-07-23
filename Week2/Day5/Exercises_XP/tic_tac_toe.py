
game_board = [
    ['*', '*', '*', '*', '*', '*','*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', 't1', ' ','|', ' ', 't2', ' ', '|', ' ', 't3', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', '-', '-', '-','|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', 't4', ' ','|', ' ', 't5', ' ', '|', ' ', 't6', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', '-', '-', '-','|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', 't7', ' ','|', ' ', 't8', ' ', '|', ' ', 't9', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', '*','*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
]


def print_board():
    border = '#'
    for row in game_board:
        for col in row:
            if col == '*':
                print(border, end='')
            elif col[0] == 't':
                print(col[1], end='')    
            else:
                print(col, end='')
        print('')   

def game_positions():
    positions = []
    for row_index, row in enumerate(game_board):
        for col_index, element in enumerate(row):
            if element[0] == 't':
                positions.append((row_index, col_index))
    position_dict = {}   
    num = 1         
    for index in positions:
        position_dict[num] = index
        num += 1
    return position_dict
    
used_position = []
def player_input(player, position_dict):
    color_reset = '\033[0m'  # Reset color to default
    color_red = '\033[31m'  # Red text
    color_green = '\033[32m'  # Green text
    if player == 'X':
        player = color_red + 'X' + color_reset
    else:
        player = color_green + "O" + color_reset

    position = int(input(f'{player}, please choose a position from 1-9: '))
    while position in used_position:
        position = int(input(f'position {position} is already occupied. Please choose another: '))
    used_position.append(position)    
    board_position = position_dict[position]
    game_board[board_position[0]][board_position[1]] = player          
       
                  
def game_player():
    player1 = input('Player 1, please choose X or O: ').upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f'Player 2, you are {player2}.')
    return player1, player2

def check_win(play_turn):  
    if game_board[1][4] == game_board[1][8] == game_board[1][12]:
        print(f'{play_turn} win!')
        return True
    elif game_board[1][4] == game_board[3][8] == game_board[5][12]:
        print(f'{play_turn} win!')
        return True
    elif game_board[3][4] == game_board[3][8] == game_board[3][12]:
        print(f'{play_turn} win!')
        return True
    elif game_board[5][4] == game_board[5][8] == game_board[5][12]:
        print(f'{play_turn} win!')
        return True
    elif game_board[5][4] == game_board[3][8] == game_board[1][12]:
        print(f'{play_turn} win!')
        return True
    elif game_board[1][4] == game_board[3][4] == game_board[5][4]:
        print(f'{play_turn} win!')
        return True
    elif game_board[1][8] == game_board[3][8] == game_board[5][8]:
        print(f'{play_turn} win!')
        return True
    elif game_board[1][12] == game_board[3][12] == game_board[5][12]:
        print(f'{play_turn} win!')
        return True    

def check_step(player, position_dict):
    print('')
    player_input(player, position_dict)
    print_board()

def play():
    print_board()
    position_dict = game_positions()
    player = game_player()
    stop = False
    end = False
    steps = 0
    while not end and not stop:
        for i in range(0, 2):
            if steps == 9:
                end = True
                break
            play_turn = player[i]
            check_step(play_turn, position_dict)
            stop = check_win(play_turn)
            if stop:
                break
            steps +=1                         

play()    