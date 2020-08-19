#Given an NxN matrix, rotate it by 90 degrees. You should perform this operation in-place, using only constant memory.

#Example:
#starting matrix:
#[
# [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
#]
#once rotated by 90 degrees, the matrix becomes:
# [
#  [7, 4, 1]
#  [8, 5, 2]
# [9, 6, 3]
#]


class Solution(object):
    def rotate(self, matrix):
        size = len(matrix[0])
        # Since you technically move 2 numbers on a side, we divide the work in half :)
        for coordX in range(int(size/2)):
            for coordY in range(coordX, size-coordX-1):
                temp = matrix[coordX][coordY]
                # Top-left copies bottom left's value.
                matrix[coordX][coordY] = matrix[size-coordY-1][coordX]
                # Bottom-left copies bottom right's value.
                matrix[size-1-coordY][coordX] = matrix[size-1-coordX][size-1-coordY]
                # Bottom-right copies top-right's value.
                matrix[size-1-coordX][size-1-coordY] = matrix[coordY][size-1-coordX]
                # Top-right copies top-left's value, which we overwrote. This is where temp is useful.
                matrix[coordY][size-1-coordX] = temp

        
        

