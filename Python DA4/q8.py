def fib(n):
    if n<0:
        return "Invalid"
    elif n in [0,1]:
        return n
    else: 
        return fib(n-2)+fib(n-1)
i=0
while True:
    a = fib(i)
    if a > 50:
        break
    print(a)
    i+=1
