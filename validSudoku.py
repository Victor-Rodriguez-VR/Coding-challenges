def validate_sudoku_board(board):
  for row in range(9):
    if(validateRow(board[row],9) == False):
      return False

  for column in range(9):
    if((validateColumn(board, column,9) == False)):
      return False

  blocks = [0,3,6]
  for block in blocks:
    if(validate3s(board,block) == False):
      return False
  return True
  
def validateRow(row, howFar):
  answers = [False] * 9
  for slot in row:
    if(slot != "."):
      numberInSlot = int(slot)
      if(answers[numberInSlot-1] != True):
        answers[numberInSlot-1] = True
      else:
        return False
  return True

def validateColumn(board, column, howFar):
  answers = [False] * 9
  for slot in range(howFar):
    if(board[slot][column] != "."):
      numberInSlot = int(board[slot][column])
      if(answers[numberInSlot-1] != True):
        answers[numberInSlot-1] = True
      else:
        return False
        
  return True

def validate3s(board,howFar):
  for row in range(9):
    if(row % 3 ==0):
        answers = [False] * 9
    for slot in range(howFar,howFar+3):
      if(board[row][slot]!=  "."):
        numberInSlot = int(board[row][slot])-1
        if(answers[numberInSlot-1] != True):
            answers[numberInSlot-1] = True
        else:
            return False
  return True

userInput = input("Select 1 for your own sudoku board.\n Select 2 for an example board")
board1 = [
["5","3",".", ".","7",".", ".",".","."],
["6","4","7", "5","9","8", ".","2","1"],
[".","9","8", ".",".",".", ".","6","."],

["8",".",".", ".","6",".", ".","5","3"],
["4",".",".", "8",".","3", ".",".","7"],
["7",".",".", ".","2",".", ".",".","6"],

[".","6",".", ".",".",".", "2","8","."],
[".",".",".", "4","1","9", ".",".","5"],
[".",".",".", ".","8",".", ".","7","9"]
]
if(input !=1):
  board1= userInput
print(validate_sudoku_board(board1))