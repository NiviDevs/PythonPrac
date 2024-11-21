def countMatchingChars(s1, s2):
    count = 0 
    for i in range(len(s1 if s1 < s2 else s2)): 
        if s1[i] == s2[i]: #comparing characters
            count += 1
    return count

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print(countMatchingChars(s1, s2))
