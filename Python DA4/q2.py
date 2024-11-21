def remDupe(l):
    lis = list(dict.fromkeys(l))
    return lis
a = list(map(int,input("Enter numbers : ").split()))
print("Your input : ",a)
print("Distinct : ",remDupe(a))
