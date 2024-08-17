#function:là hàm, với mđ tái su dung, giup code gon hon, tuong minh hon
#arguments
"""
tham so: la cai truyen vao
khi goi ham ra truyen vao 1 bien nao do thì cai bien do goi la doi so:
doi so mac dinh de o phia cuoi
doi so voi tu khoa: viet tu khoa ra
*args:sdung khi chua biet so luong bien, tong hop lai thanh 1 tuple
*kwargs: thu thap cac doi so dau vao tao thanh 1 dictionary
"""

# def hello(name:str,age:int = 40):
#     """
#     first function
#     """
#     # print(f'hello {name}',age)
#     return f'Hello {name} {age}'
# # string=hello("HoaThu",18)
# string=hello(age=20,name='HoaThu')
# print(string)
# def sum(a:int):
#     """
#     ham tinh tong cai so le cua 1 list
#     """
#     n=int(input("Nhap n phan tu cua list:"))
#     a=[int(input(f'a[{i}]=')) for i in range(n)]
#     sum=0
#     for i in a:
#         if i % 2 !=0:
#             sum+=i
#     return sum
# print(sum(5))
# def tong(l:list):
#     sum=0
#     for i in l:
#         if i%2!=0:
#             sum+=i
#     return sum
# my_list=(1,2,3,4,5)
# print(tong(my_list))
# def tong(*args) -> int:
#     print(args)
#     return sum(args)
# a,b,c,d,e,f=1,2,3,4,5,6
# result=tong(a,b,c,d,e,f,25,99)
# print(result)
import json
# def sinhvien(**kwargs) -> int:
#     print(kwargs)
# result= sinhvien(name="HoaThu",
#                  age=18,
#                  city='Hanoi')
# print(result)
# def tong(a,b,*args,**kwargs):
#     print(args)
#     print(a)
#     print(b)
# tong(1,2,3,4,5,6,7,8,9)
# def outer(a,b):
#     def inner(c,d):
#         return c+d
#     return inner(a,b)
# result=outer(1,2)
# print(result)
# cout=print
# cout("hello")
'''
lambda(ham an danh):sd khi khong can tai su dung ham do
cu phap: lambda: arguments : return
'''
# result=lambda a,b: a+b
# print(result(1,2))
# -------------------------------------------------------
"""
nhap vao 1 so n.In ra man hinh dah sach cac so fibonaci được mũ ba từ 0 đến n
ví dụ: n=5
output=[0,1,1,88,27]
"""
# def fibonaci(n:int):
#     f0=0
#     f1=1
#     fn=1
#     print(f0,f1,fn,end='\t')
#     for i in range(1,n-2):
#         c=list()
#         f0 = f1
#         f1 = fn
#         fn = f0 + f1
#         print(fn,end='\t')
#
# n=int(input("Nhap so n ban thich:"))
# b=[fibonaci(5)]
# for i in len(b):
#     c=b*b*b
#     print(c)
#

# def fibonaci2(n:int):
#     l=[0,1]
#     if n==0:
#         return []
#     elif n==1:
#         return [0]
#     else:
#         for i in range(2,n):
#             l.append(l[i-1]+l[i-2])
#         return l
# cube= lambda x: x**3
# n=int(input("Nhap n:"))
# print(list(map(cube,fibonaci2(n))))
a=list(input("Nhap a:"))
count=0
for i in a:
    count=count+1
    if a[0] ==0:
        print("hop le")
    # print(i)
    else:
        print("k hop le")
print("s=",count)