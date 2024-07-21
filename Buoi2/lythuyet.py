'''a=2023
print(2023)
a = float(input("a="))
print(type(a),a)'''
#string
#a=input("mystring=")
#b=str("6")
#print(a+b)
'''
a="hoathu"
print(a)
print(a[0]) #chi so dau
print(a[-6])
print(a[0:3]) #lay cac ky tu mk muon print(a[:3])
#sliced_string
print(len(a))
#print(type(a),a,sep="\n")
a = "i love python"
print("truoc khi thay doi")
print(a)
a[0]="Y"
print("sau khi thay doi0")
print(a)
print(a[0],a[9]) '''
#list
'''my_list = [1,2,3,'hello']
print("my lisrt: ",my_list)
print("type: ", type(my_list))
print(my_list[1])
print(my_list[0:3]) #bat dau lay tu chi so 0 den chi so 3 nhung khong lay so 3'''
#tuple
'''my_tuple=(1,2,3,4,'hello')
print(my_tuple)
print(type(my_tuple))'''
#dic
''' import pprint
my_dic= { #cac cap keys khong cho phep trung lap
    "keys": "values",
    "keys1": "values",
    "keys2": "values",
    "keys3": "values",
}
pprint.pprint(my_dic) '''
'''print(type(my_dic))
lop = {
    '2023603165' : {
        "ten":" T N",
        "gioi tinh" : "G"
}
} '''
#toan tu so hoc
'''a=10
b=3
print("a+b = ",a+b)
print("a-b = ",a-b)
print("a*b = ",a*b)
print("a/b = ",a/b)
print("a%b = ",a%b)
print("a**b = ",a**b)
print("a//b = ",a//b)
# print("a+b = ",a+b) '''
#toan tu so sanh
'''a=25
b=6
print("a==b",a==b)
print("a!==b",a!=b)
print("a>=b",a>=b)
print("a<=b",a<=b)'''
#toan tu logic
'''a=10
b=6
print(a<b and a<10)
print(a>b or a<1)
print(not(a>5))'''
#toan tu thanh vien
''' a='i love em'
print('l' in a)
if 'i' in a:
    print("hello")
else :
    print("leke") '''
#toan tu nhan dang
''' a = 25
b = 6
print(id(a))
print(id(b))
print(a is b)
print(a==b) '''
# is la cap so sanh cao hon, no so sanh them ca kieu du lieu
# if else
''' if <expr> :
    <statement>
    
'''
# if 5<4 :
#    print("yes")
# elif 5==5:
#     print("keke")
# else:
#     print("chuan")
''' a=1
if a%2==0:
    result= a*2
else :
    result = a*3
print(result)
result = a*2 if a%2==0 else a*3

print(result) '''
#vong lap
'''
for <var> in <interable> :
    <statement(s)>
'''
# my_list1=[1,2,3,'haha']
# my_tuple=(1,2,5,'hehe')
# for i in my_list1:
#     print(i, end='\t')
# for j in my_tuple:
#     print(j,end='\n')
# for i in range(0,10,1):
#     print(i, end=" ")
a=0
while a<10:
    a += 1
    if a==5:
        continue
    print(a, end=' \t')
