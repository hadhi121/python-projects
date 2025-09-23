name  = input('type your name: ')
print('Welcome ',name,'to this TIC-TAC-TOE game')

import random

board = ['-','-','-',
         '-','-','-',
         '-','-','-']
user = ''
computer_symbol = ''
para = ''
winner = 0


#printing the  BOARD
def board_image(para):
    print(board[0] +' | ' + board[1] + ' | ' + board[2])
    print('______________')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('______________')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])



#take the player input
def player_input(para):
    p_input = int(input('enter a num from 1-9: '))
    if p_input >= 1 and p_input <= 9 and board[p_input - 1] == '-':
        board[p_input-1] = user
    else:
        print('invalid option')

#check for win or tie
def check_horizontal(para):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != '-':
        winner = board[7]
        return True
    
def check_row(para):
    global winner
    if board[0] == board[3] == board[6] and board[3] != '-':
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != '-':
        winner = board[5]
        return True
    

def check_diagonal(para):
    global winner
    if board[0] == board[4] == board[8] and board[4] != '-':
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[4]
        return True

def checkWin():
    global winner_name
    if check_horizontal(para) or check_row(para) or check_diagonal(para):
       winner_name = f'the winner is {winner}'
       return True
    return False

def check_tie(para):
    if '-' not in board and (check_horizontal(para) != True or check_diagonal(para) != True or check_row(para)!=True):
        board_image(para)
        print('it is a tie match!!!')
        return True
    return False

#switch the player
'''def switch_player():
    global user
    if user== 'X':
        computer_symbol = 'O'
    else:
        user = 'X'  '''

#COMPUTER
def computer(para):
    while True:
       random_number = random.randint(0,8)
       if board[random_number] == '-':
        board[random_number] = computer_symbol
        break
#CHOOSE SYMBOL (NEW)
while user not in ['X','O']:
    user = input('Pick a symbol "X" or "O": ').upper()
    if user == "X":
        computer_symbol = 'O'
        break
    else:
        computer_symbol = 'X'
        break
print(f"You are {user} , Computer is {computer_symbol}\n") 

#if user picks O then computer moves FIRST
if user == 'O':
    computer(para)

#MAIN GAME LOOP
while True:
    board_image(para)
    player_input(para)
    if checkWin():
        board_image(para)
        print('CONGRATS',winner_name)
        break
    if check_tie(para):
        board_image(para)
        break
 
    computer(para)

    if checkWin():
        board_image(para)
        print('CONGRATS',winner_name)
        break
    if check_tie(para):
        board_image(para)
        break


print('goodbye!! ')