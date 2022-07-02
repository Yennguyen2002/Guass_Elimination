arr = [[1, 2, -1, -1], [2, 2, 1, 1], [3, 5, -2, -1]] # có nghiệm

#arr = [[1, -2, 3, -3], [2, 2, 0, 0], [0, -3, 4, 1],[1,0,1,-1]] # vô số nghiệm

#arr = [[1, 2, -1, -1], [0, 1, 4, 3], [0, 0, 0, 2]] #vô nghiệm

# Hiện thị ma trận
def showMatrix():
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end='\t')
        print()


# Kiểm tra cột bằng 0 , nếu cột = 0 thì duyệt cột tiếp theo
def check_Zero_Col(arr, col, row):
    while (col < len(arr[0])):
        for i in range(row, len(arr)):
            if (arr[i][col] != 0):
                return col
        col = col + 1
    return -1


# Kiểm tra vị trí khác 0 có nằm đầu cột
def find_Row_Zero(arr, row, col):
    for i in range(row, len(arr)):
        if (arr[i][col] != 0):
            return i
    return -1


# Đổi dòng
def swapRow(arr, row, temp):
    for i in range(len(arr[0])):
        arr[row][i], arr[temp][i] = arr[temp][i], arr[row][i]


# di = di + k.dj
def add_Row(arr, col, row):
    for i in range(row + 1, len(arr)):
        k = arr[i][col]
        for j in range(col, len(arr[0])):
            arr[i][j] = arr[i][j] - k * arr[row][j]


# Gauss Elimination
def gauss_Elimination(arr):
    n = len(arr)
    m = len(arr[0])
    row = col = 0
    temp = 0
    # B1
    while (row < n):
        col = check_Zero_Col(arr, col, row)
        if (col == -1):
            return arr
        print("---------------------")
        # B2
        row = find_Row_Zero(arr, row, col)
        if row != temp:
            swapRow(arr, row, temp)
            print("swap row!")
        # B3
        # Nhan voi 1/a
        if (arr[row][col] != 1):
            a = 1 / arr[row][col]
            for i in range(row, n):
                for j in range(col, m):
                    arr[i][j] *= a

        add_Row(arr, col, row)

        showMatrix()

        row += 1
        temp = row
    return arr


def back_substitution(arr):
    n = len(arr)
    m = len(arr[0])
    row = n
    col = m

    # Kiểm tra hệ phương trình vô số nghiệm
    count = 0  # số dòng = 0
    for i in range(n):
        if (all([x == 0 for x in arr[i]])):
            count = count + 1
    if (n - count < m and count != 0):
        print("Hệ phương tình vô số nghiệm")
        return

    # Kiểm tra hệ phương trình vô nghiệm
    for i in range(n):
        if (all([arr[i][x] == 0 for x in range(len(arr[i]) - 1)])):
            if (arr[i][m - 1] != 0):
                print("Hệ phương tình vô nghiệm")
                return

    # Hệ phương trình có nghiệm
    print("---------------------")
    print("Hệ phương trình có nghiệm")
    newArr = []
    for i in range(n - 1, -1, -1):
        newArr.insert(0, arr[i][n] / arr[i][i])
        for k in range(i - 1, -1, -1):
            arr[k][n] -= arr[k][i] * newArr[0]
    print(newArr)


array = gauss_Elimination(arr)
back_substitution(array)
