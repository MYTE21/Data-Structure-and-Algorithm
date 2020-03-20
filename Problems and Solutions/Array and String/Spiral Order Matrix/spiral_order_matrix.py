def spiral_matrix_to_linear(matrix, m, n):
    direction = 0 # 0 is right, 1 is down, 2 is left, 3 is up
    top = 0
    bottom = m-1
    left = 0
    right = n-1
    linear_array = []

    while top<=bottom and left<=right:
        if direction == 0:
            for i in range(left, right+1):
                linear_array.append(matrix[top][i])
            top += 1
        elif direction == 1:
            for i in range(top, bottom+1):
                linear_array.append(matrix[i][right])
            right -= 1
        elif direction == 2:
            for i in range(right, left-1, -1):
                linear_array.append(matrix[bottom][i])
            bottom -= 1
        else:
            for i in range(bottom, top-1, -1):
                linear_array.append(matrix[i][left])
            left += 1

        direction = (direction+1) % 4

    return linear_array

if __name__ == '__main__':
    m = int(input("Enter the row number : "))
    n = int(input("Enter the coloum number : "))
    matrix = [[int(input()) for x in range (n)] for y in range(m)]
    linear_array = spiral_matrix_to_linear(matrix, m, n)
    print("The linear array  is : ", linear_array)
