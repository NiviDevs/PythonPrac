list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
lis1 = list1.copy()

print("Using for loop")
for i in range(4):
    list1[i] = list1[i]+ list2[i]
print(list1)

print("Using zip fn")
lis3 = list(map(lambda x : "".join(i for i in x), zip(lis1,list2)))
print(lis3)
