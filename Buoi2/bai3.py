import math
print("Nhap he so cua pt bac 2 mot an ax^2+bx+c:")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
denta=b*b-4*a*c
if denta>0:
    x1=(-b+ math.sqrt(denta))/(2*a*c)
    x2= (-b - math.sqrt(denta)) / (2 * a * c)
    print("phuong trinh co 2 nghiem la: ",x1)
elif denta==0:
    x1=(-b)/(2*a)
    print("phuong trinh co 1 nghiem kep x1=x2 la: ",x1)
else:
    print("phuong trinh vo nghiem")