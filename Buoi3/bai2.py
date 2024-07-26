k=int(input("Nhap k phan tu ban muon:"))
a=list()
print("Nhap cac phan tu cho list a: ")
a=[int(input(f'mylist[{i}]=')) for i in range(k)]
n=int(input("Nhap n hang cho ma tran:"))
m=int(input("Nhap m cot cho ma tran:"))
if k<n*m:
    print("NO")
else:
    matrix = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        matrix.append(row)
    print("Ma trận là:")
    for row in matrix:
        print(row)