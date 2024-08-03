my_tup=tuple()
my_list=list(my_tup)
n=int(input("Nhap n phan tu cho tup:"))
print("Nhap cac phan tu cho tup:")
a=[str(input(f'mytup[{i}]=') ) for i in range(n)]
for i in a:
    my_list.append(i)
my_tup=tuple(my_list)
numbers = tuple(int(x) for x in my_tup if x.isdigit())
if numbers:
    tbc=(sum(numbers))/ (len(numbers))
    print(tbc)
else:
    print("khong co so trong 1 tup")