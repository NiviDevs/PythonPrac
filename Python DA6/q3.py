def gcd(a,b):
    if a <= 1 or b <= 1:
        return a
    else:
        return gcd(b, a % b)

print(gcd(int(input("Enter number 1: ")),int(input("Enter number 2: "))))