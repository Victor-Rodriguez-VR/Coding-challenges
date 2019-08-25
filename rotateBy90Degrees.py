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




def rotate_list(matrix):
        size = len(matrix)
        # Since you technically move 2 numbers on a side, we divide the work in half :)
        for coordX in range(int(size/2)):
                for coordY in range(coordX, size-coordX-1):
                        # The x and y of where are going to rotate.
                        lastX = size-coordX-1
                        lastY = size-coordY-1
                        # Since we copy in place, we need an extra varaible to assure no data gets lost :)
                        temp = matrix[coordX][coordY]
                        # Top-left copies bottom left's value.
                        matrix[coordX][coordY] = matrix[lastY][coordX]
                        # Bottom-left copies bottom right's value.
                        matrix[lastY][coordX] = matrix[lastX][lastY]
                        # Bottom-right copies top-right's value.
                        matrix[lastX][lastY] = matrix[coordY][lastX]
                        # Top-right copies top-left's value, which we overwrote. This is where temp is useful.
                        matrix[coordY][lastX] = temp
                # Returns the newly rotated matrix.
                return matrix




