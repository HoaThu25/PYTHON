s1 = input("Nhập phần tử cho s1: ")
s2 = input("Nhập phần tử cho s2: ")
s1_reversed = s1[::-1]
print("Đảo ngược của chuỗi s1:", s1_reversed)
a=int(input("Nhap so nguyen a ban thich:"))
b=int(input("Nhap so nguyen b ban thich:"))
if 1 <=a < b <= len(s2) :
    s2_reversed=s2[:a] + s2[a:b+1][::-1] + s2[b+1:]
print(s2_reversed)

s3=" "
for i in range(len(s2)):
    if i % 2 != 0:  #  chọn các ký tự ở vị trí lẻ
        s3 += s2[i]  # Nối ký tự vào chuỗi s
print(s3)

s=""
for i in range(max(len(s1), len(s2))):
    if i<len(s1):
        s+=s1[i]
    if i<len(s2):
        s+=s2[i]
print(s)

s=s1[0:1]
ss=s2[0:1]
s1=ss+s1[1:]
s2=s+s2[1:]
print(s1)
print(s2)