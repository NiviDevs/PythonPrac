def isPrime(num):
    p = False
    num = abs(num) if num < 0 else num
    if num == 0:
        return False
    elif num <= 2:
        return True
    else:
        for i in range(2, num // 2 + 2):
            if num % i == 0:
                return False
            else:
                p = True
    return p

r = range(int(input("Enter lower limit: ")),int(input("Enter upper limit: "))+1)
num = r[1]
c = 0
while num in r:
    if not isPrime(num):
        print(num)
        if num%2==0:
            c+=1
    num+=1

print("No. of even numbers : ",c)
