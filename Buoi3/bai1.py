n=int(input("Nhap n so nguyen duong ban muon:"))
mylist=list()
print("Nhap cac phan tu cho list:")
mylist=[int(input(f'mylist[{i}]=') ) for i in range(n)]
print(mylist)
x=int(input(("Nhap so x ban muon:")))
cout=0
for i in range(len(mylist)):
    if i==x:
        cout+=1
print("So lan xuat hien cua x trong mylist la:",cout)

mylist[2:8]=[8, 5, 4, 0, 1, 3]
print(mylist)

print("Gia tri lon nhat cua list la: ",max(mylist))
print("Gia tri nho nhat cua list la: ",min(mylist))

y=int(input("Nhap so y ban muon: "))
mylist.insert(0,y)
print(mylist)

is_increasing = True
is_decreasing = True
for i in range(len(mylist) - 1):
    if mylist[i] > mylist[i + 1]:
        is_increasing = False
    if mylist[i] < mylist[i + 1]:
        is_decreasing = False
if is_increasing:
    print("TĂNG")
elif is_decreasing:
    print("GIẢM")
else:
    print("NO")

print("Nhap lai cac phan tu o list cu:")
mylist=[int(input(f'mylist[{i}]=') ) for i in range(n)]
mylist1=list()
for i in range(1,n+1):
    tong= sum(mylist[0:i])
    mylist1.append(tong)
print("List mới là:")
print(mylist1)

import math
list=[94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
list1=sorted(list)
print("List sx tang dan theo gia tri la: ",list1)
list2=sorted(list,key=abs)
print("List sx tang dan theo gia tri tuyet doi la:",list2)
