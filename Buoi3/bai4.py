s=input("Nhap ho va ten cua 1 thanh vien:")
s.strip()
s1=""
for i in s.split():
    s1=i
    print(s1.title(),end=' ')