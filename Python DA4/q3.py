def isPrime(num):
    p = False
    num = abs(num) if num < 0 else num
    if num == 0:
        return False
    elif num <=2:
        return True
    else:
        for i in range(2,num//2 + 2):
            if num%i == 0:
                return False
            else:
                p = True
    return p

a = isPrime(271)
print(a)