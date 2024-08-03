#tuple: tương tự list,khac list 1 cai la khong the thay doi duocj gia tri
'''
dong goi va mo goi tuple
tuple
'''
#khai bao
# tup=tuple()
# tup1=(1,"hello",["some text",1,2])
# tup2=(1,"hello",["some text",1,2])
# print(f"tup={tup}\\t({type(tup)}")
# print(f"tup={tup1}\\t({type(tup1)}")
# print(f"tup={tup2}\\t({type(tup2)}")
# print("tup1[3]",tup1[2][1])
# print(tup1)
# tup1=list(tup1)
# tup1[1]="HI"
# tup1=tuple(tup1)
# print(tup1)
#set
# set={1,2,3,"hello",4}
# # print(set)
# #dung add()(them 1) or update()(them nhieu) de them cac ptu vao set
# set.add(5)
# set.update([2,3,22,3])
# print(set)
'''
xoa item ra khoi set: remove, pop,clear,discard
clear:xoa het tat ca
pop:
'''
# set.remove(2)
# set.pop()
# set.clear()
# set.discard(96)
# print(set)
'''
set se in ra cac phan tu 1 cach ngau nhien, khi them 1 hoac nhieu phan tu khac vao thi no se sx ngau nhien cac phan tu
moi va giu nguyen cac phan tu cu 

cac phuong thuc xac thuc:
issubset() ktra xem co phai la tap con hay khong
issuperset
'''
# s={1,2,3,4,5,6}
# s1={2,3,4}
# s1={'blue','black','green'}
# s2={'black','pink','orange'}
# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s1 ^ s2)


string="Hoc lap trinh Python cung HIT"
#ouput: ('H','O',...)
# s=string.upper()
# s1=s.split()
# for i in s1:
#     print(i)
#c1: dung for
result=[]
# for char in string:
#     if char == " ":
#         continue
#     result.append(char)
# print(tuple(result))

#cach2
# for index in range(len(string)):
#     if string[index] == " ":
#         continue
#     result.append(string[index])
# print(tuple(result))

#c3: dung list comprehension
# result1=[char for char in string if char !=" "]
# print(tuple(result1))
# cout=0
# char_o=[cout+1 for char in result1 if char == "h"]
# print(len(char_o))

#cho 1 danh sach, in ra phan tu lon thu 2 trong danh sach
# n= int(input("Nhap vao n so nguyen:"))
# print("Nhap cac phan tu cho list")
a=[22,22,36,548,2515]
# a=[int(input(f'a[{i}]=') ) for i in range(n)]
a =set(a)
print(a)
l =list(a)
print(l[-2])

