def chuanhoa(n):
    somoi=''.join(filter(str.isdigit,n))
    if len(somoi) != 10 or somoi[0]!='0':
        return "Invalid phone number"
    return somoi
n=str(input("Nhap sdt:"))
print(chuanhoa(n))