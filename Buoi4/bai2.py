setA=set()#ban 1
setB=set()#ban 2
setA=list(setA)
setB=list((setB))
n=int(input("Nhap so sv muon dki o ban 1: "))
setA=[str(input(f'setA[{i}]=') ) for i in range(n)]
setA=set(setA)
m=int(input("Nhap so sv muon dki o ban 2: "))
setB=[str(input(f'setB[{i}]=') ) for i in range(m)]
setB=set(setB)
a=setA & setB
if a:
    print("Co sv dki ca 2 ban! ")
    print("Nhap phim 1 de xem danh sach")
    b = int(input())
    if b==1:
        print(a)
    else:
        print("Sai cu phap")
else:
    print("Khong co sv dki o 2 ban")

b=setA | setB
if b:
    print("Danh sach sv dki o ca 2 ban la: ",b)
else:
    print("khong co!!")

c=setA - setB
if setA:
    print("DS sv dki o ban 1 ma khong dki o ban 2 la: ",c)
else:
    print("khong co")
