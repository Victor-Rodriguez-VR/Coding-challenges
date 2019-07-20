def rotate_list(matrix):
    size = len(matrix)
    for coordX in range(int(size/2)):
        for coordY in range(coordX, size-coordX-1):
            lastX = size-coordX-1
            lastY = size-coordY-1
            temp = matrix[coordX][coordY]
            matrix[coordX][coordY] = matrix[lastY][coordX]
            matrix[lastY][coordX] = matrix[lastX][lastY]
            matrix[lastX][lastY] = matrix[coordY][lastX]
            matrix[coordY][lastX] = temp
    return rotate_list


