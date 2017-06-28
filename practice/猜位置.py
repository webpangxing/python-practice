from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

# 循环4次跳出游戏
for turn in range(4):
    Turn = turn + 1
    guess_row = int(input("猜行:"))
    guess_col = int(input("猜列:"))

    if guess_row == ship_row and guess_col == ship_col:
        print ("祝贺! 你击沉了我的战舰！")
        break #回答正确，跳出循环0
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("哎呀，这不在海洋")
        elif(board[guess_row][guess_col] == "X"):
            print ("你已经猜过这个位置了")
        else:
            print ("你没能对我的战舰造成伤害！")
            board[guess_row][guess_col] = "X"
    print (Turn)
    print_board(board) 