n = 5
for i in range(0,n,2):
    print(str.center("*"*(i+1), n))
    
    
i=0
while i <= n:
    print(str.center("*" * (i + 1), n))
    i+=2

def pyramid(n,counter=1):
    if counter > n:
        return
    print(str.center("*"*counter,n))
    pyramid(n,counter+2)

pyramid(5)

