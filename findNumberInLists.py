def matrixSearch(matrix, target):
  rowIndex = 0
  while rowIndex < len(matrix):
    if( target >= matrix[rowIndex][0] and target<= matrix[rowIndex][-1]):
      if (searchRow(matrix[rowIndex], target)) == 1:
        return 1
      else:
        return 0
    else:
      rowIndex+=1
def searchRow(currentRow, target):
  start = 0
  end = len(currentRow)
  while start<end:
    pivot = (end - start) // 2 +1
    if(currentRow[pivot] == target):
      return 1
    if( target < currentRow[pivot]):
      end = pivot
    else:
      start = pivot+1
  return 0
 
matrix = [
  [1,3,5,7],
  [10,11,16,20],
  [23,30,34,50]
]
print(matrixSearch(matrix, 37))