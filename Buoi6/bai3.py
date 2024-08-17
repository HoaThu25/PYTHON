def calculate(t,*args) :
    if t=='+':
        return sum(args)
    elif t=='x':
        tich = 1
        for i in args:
            tich*=i
        return tich
    elif t=='min':
        return min(args)
    elif t=='max':
        return max(args)
    else:
        return 'Invalid operation'
print("Nhập 1 trong các phép tính:+,x,min,max! ")
t = str(input("Phep tinh:"))
print(calculate(t,1,2,3,4,5))

