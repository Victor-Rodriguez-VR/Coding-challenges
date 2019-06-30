# Given a tic-tac-toe board as a two-dimensional array (aka list), determine the winner! There are 0s, representing an empty space, 1 representing the first player, and 2 representing the second player.

tic_tac_toe_row = [
  [1,1,1],
  [0,2,0],
  [2,0,2]
]

tic_tac_toe_column = [
  [2,1,0],
  [0,1,0],
  [0,1,2]
]

tic_tac_toe_diag = [
  [2,0,1],
  [0,1,2],
  [1,0,2]
]

def tic_tac_toe_ROW(board):
  for row in board:
    if(row[0] == row[1] == row[2] and row[0]!= 0):
      return row[0]
  return 0
    
def tic_tac_toe_COLUMN(board):
    for col in range(3):
      if(board[0][col] == board[1][col] == board[2][col] and board[0][col]!= 0 ):
        return (board[0][col])
    return 0
      
def tic_tac_toe_diagonal(board):
  if(board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0):
    return board[0][0]
  elif(board[0][2] == board[1][1] == board[2][0] and board[0][2]!= 0):
    return board[0][2]      
  return 0
  

print(tic_tac_toe_ROW(tic_tac_toe_row)) # 1
print(tic_tac_toe_COLUMN(tic_tac_toe_column))
print(tic_tac_toe_diagonal(tic_tac_toe_diag)) #