def sumprod(l):
    s,prod=0,1
    for i in l:
        s+=i
        prod*=i
    return s,prod
print("Sum,Product = ", sumprod([1,1,3]))

