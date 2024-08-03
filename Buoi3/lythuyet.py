# # # #string gia tri khong the thay doi duoc/ dung bang ma asci
# # # # dung 3 dau " de viet chuoi nhieu dong
# # # # chuoi tran se khong k quan tam den thu gọi là escape sequence
# # # "dinh dang chuoi theo so nguyen"
# # # my_string="     aukay    ke prou"
# # # print(my_string)
# # # print("upper string:", my_string.upper())
# # # print("lower string:", my_string.lower())
# # # print("string[1:3]:", my_string[1:3])
# # # print("splitted string:", my_string.split())
# # # print("splitted string:", my_string.strip())
# #
# # my_string= "-"
# # my_list = ['this is',"first","time","hehe"]
# # print(my_string.join(my_list))
# # # print('-'.join(my_list))
# # joined_string='-'.join(my_list)
# # # print(joined_string.find('is',2))
# # replaced_string=joined_string.replace('is','keek')
# # print(replaced_string)
# # print("is upper string:",joined_string.isupper())
# # print(upper_string:=joined_string.upper()) #viet tat
# # print("is lower string:",joined_string.islower())
# # mystring="02648154"
# # print("is digit string:",mystring.isdigit())
# # space_string='               '
# # print("space string:", space_string.isspace())
#
# s=str(input("Nhap 1 xau ky tu ban thich:"))
# print(s)
# s1=s.split()
# print(len(s1))
#list: giong mang, lưu tru cac du lieu, co the chua nhieu kieu du lieu, co the thay doi gia tri cua list
#khoi tao list: dung cap dau []. dung slicing de cat cac phan tu trong list
# dao nguoc phan tu
# my_list=list() #list rong
# my_list=[]
# my_list=[1,2,3,4,'hehe','jhahha',[6,7,8,9]]
# # for i in my_list:
# #     print(i)
# # for index, value in enumerate(my_list):
# #     # print(index,value)
# #     print(f'index:{index} \t value:{value}')
# print(my_list[4])
# print(my_list[6][2])
# my_list[6][2]= 56
# print(my_list)
# my_list = list()
# for i in range(10):
#     if i%2==0:
#         my_list.append(i)
# print(my_list)
# my_list = [i**2 if i**2%2==0 else "none" for i in range(10)  ]
# mylist = [i for i in range(10)]
# mylist1 = [i for i in range(10) if i%2==0]
# print(my_list)
# print(mylist)
# print(mylist1)
# tinh tong cac chan su dung list_comprehension 1->1e5
'''import time
start_time=time.time()
my_list= list()
for i in range(1,int(1e5)):
    if i%2==0:
        my_list.append(i)
print(sum(my_list))
end_time=time.time()
print("time", end_time-start_time)'''
# list_comprehension
'''import time
start_time=time.time()
mylist1 = [i for i in range(1, int(1e5)) if i%2==0]
print(sum(mylist1))
end_time=time.time()
print("time", end_time-start_time)'''
# old_list=[1,2,3]
# old_list1=[1,2,3]
# print(id(old_list))
# print(id(old_list1))
# new_list=old_list.copy()
# old_list.append(1000000)
# print(new_list)
# print(id(new_list))

# n= int(input("Nhap vao n so nguyen:"))
# a=[int(input(f'a[{i}]=') ) for i in range(n)]
# b=[int(input(f'b[{i}]=') for i in range(n))]
#
# b=[i**2 for i in [2,9,8,3,5,1]]
# a=[2,9,8,3,5,1]
# print(b)
# a.sort()
# print(a)
# # a_sorted=sorted(a,reverse=False)
# bi=[i*2 for i in b]
# print("bi[::1]:",bi[::-1])
# c=a+bi
# c1=a.extend(bi)
# print(c)