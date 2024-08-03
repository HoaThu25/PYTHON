print("nhap vao hai so a,b:")
a=int(input("a="))
b=int(input("b="))
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a//b=",a//b)
print("a**b=",a**b)
print("a%b=",a%b)
if a > b:
    print(f"a > b")
elif a < b:
    print(f"a < b")
else:
    print(f"a == b")

print(f"a & b = {a & b}")
# a OR b
print(f"a | b = {a | b}")
# a XOR b
print(f"a ^ b = {a ^ b}")
# k. NOT a == b
print(f"not (a == b) = {not (a == b)}")
# l. a dịch phải 1 đơn vị
print(f"a >> 1 = {a >> 1}")
# m. a dịch trái 1 đơn vị
print(f"a << 1 = {a << 1}")