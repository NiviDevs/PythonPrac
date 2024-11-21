def twoAndTwo(s1):
    if len(s1) < 2:
        return "" #Empty string returned
    else:
        return s1[:2] + s1[-2:] #adding first and last two chars

print(twoAndTwo(input("Enter a string: ")))
