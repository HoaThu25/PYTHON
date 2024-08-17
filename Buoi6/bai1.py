# def kytu(a,b):
#     # print("Nhap 2 ky tu ban thich: ")
#     # a=str(input("Nhap ky tu a:"))
#     # b= str(input("Nhap ky tu b:"))
#     if 'a'>'b':
#         return a
#     else:
#         return b
# a=str(input("Nhap ky tu a:"))
# b= str(input("Nhap ky tu b:"))
# print(kytu(a,b))
a=str(input("Nhap a:"))
b=str(input("Nhap b:"))
kytu=(lambda a, b: a if a > b else b)
result=kytu(a,b)
print(result)