x=int(input("Nhap so nguyen duong n: "))
tong=0
while x>0:
    tong+=x%10
    x//=10
print("Tong cac chu so cua n la: ",tong)

for i in range(1,x+1):
    if x%i == 0:
        print(i,end="\t")
    elif i == x:
        print("Khong co uoc nao cua so")

print("Nhap so do 3 canh cua tam giac!")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a>0 and b>0 and c>0:
    if (a**2==b**2+c**2)or (b**2==a**2+c**2) or (c**2==a**2+b**2):
        print("Tam giac nay la tam giac vuong")
    elif (a==b==c):
        print("Tam giac nay la tam giac deu")
    elif (a==b) or (b==c) or (a==c):
        print("Tam giac can")
    elif (a**2>b**2+c**2) or (b**2>a**2+c**2) or (c**2>a**2+b**2) :
        print("Tam giac la tam giac tu")
    else :
        print("Tam giac la tam giac nhon")
else:
    print("Khong phai la tam giac")