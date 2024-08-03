n=int(input("Nhap n phan tu cho xau cua ban: "))
a=[input(f'a[{i}]=')  for i in range(n)]
b=tuple(a)
print("Tuple b:",b)
count=0
for i in a:
    if i.isdigit():
        count+=1
print("Số phần tử có dạng số trong tuple b là:",count)