def tcs(n) -> int :
    tong=0
    while n>0:
        tong+=n%10
        n//=10
    return tong
def step(n):
    steps=0
    while n>=10:
        n=tcs(n)
        steps+=1
    return n,steps
x=int(input("Nhap so nguyen duong ban muon:"))
if x>0:
    tong, steps =step(x)
    print(tong, steps)
