n=int(input("Nhap so nguyen n ban thich:"))
so=[int(input(f'mylist[{i}]=') ) for i in range(n)]
thich=[1, 3, 7, 5, 9]
cout=0
thayBa=[]
for i in so:
    if i%10 in thich:
        cout+=1
        thayBa.append(i)
print(cout)
print(thayBa)
