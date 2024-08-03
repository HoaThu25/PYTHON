n=int(input("Nhap n so fibonacci ban muon tim:"))
f0=0
f1=1
fn=1
print(f0,f1,fn,end='\t')
for i in range(1,n):
    f0=f1
    f1=fn
    fn=f0+f1
    print(fn,end='\t')