def hoanvi(matrana):
    matrix_hoanvi = []
    for i in range(len(matrana[0])):
        row = []
        for j in range(len(matrana)):
            row.append(matrana[j][i])
        matrix_hoanvi.append(row)
    return matrix_hoanvi

def matran(n, m):
    matrana = []
    print("Nhap cac phan tu cho matran a: ")
    matrana = [int(input(f'mylist[{i}]=')) for i in range(n*m)]
    if n*m < 0:
        print("NO")
        return None
    else:
        matrix = []
        index = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(matrana[index])
                index += 1
            matrix.append(row)
        print("Ma trận là:")
        for row in matrix:
            print(row)
        return matrix

# Nhập số hàng và số cột cho ma trận
n = int(input("Nhap n hang cho ma tran:"))
m = int(input("Nhap m cot cho ma tran:"))

# Tạo ma trận và lưu kết quả
matrix = matran(n, m)

# In ma trận chuyển vị nếu ma trận ban đầu không rỗng
if matrix:
    matrix_hoanvi = hoanvi(matrix)
    print("Ma trận chuyển vị là:")
    for row in matrix_hoanvi:
        print(row)
