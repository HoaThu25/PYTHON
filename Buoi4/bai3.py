n=int(input("Nhap n so nguyen ban thich:"))
my_list=[int(input(f'my_list[{i}]=') ) for i in range(n)]
m=int(input("Nhap so phan tu ban muon o 2 set: "))
setA = set(map(int, input("Nhap cac phan tu o setA: ").split()))  # Nhập setA
setB = set(map(int, input("Nhap cac phan tu o setB: ").split()))  # Nhập setB
happy=0
for i in my_list:
    if i in setA:
        happy+=1
    elif i in setB:
        happy-=1
print(happy)