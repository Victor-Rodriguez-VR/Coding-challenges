def validate_sudoku_board(board):
  print("Hello!")
  for row in range(9):
    if(validateRow(board[row]) == False):
      return False

  for column in range(9):
    if((validateColumn(board, column) == False)):
      return False

  ##Validating the 3 blocks will go here :)
  return True
  
def validateRow(row):
  answers = [False] * 9
  for slot in row:
    if(slot != "."):
      numberInSlot = int(slot)
      if(answers[numberInSlot-1] != True):
        answers[numberInSlot-1] = True
      else:
        return False
  return True


def validateColumn(board, column):
  answers = [False] * 9
  
  for slot in range(9):
    if(board[slot][column] != "."):
      numberInSlot = int(board[slot][column])
      if(answers[numberInSlot-1] != True):
        answers[numberInSlot-1] = True
      else:
        return False
        
  return True
  
 
