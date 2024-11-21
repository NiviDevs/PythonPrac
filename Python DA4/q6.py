list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
out1 = []
for i in list1:
    for j in list2:
        out1.append(str(i + j))
print(out1)

out2= list(map(lambda x : "".join(i for i in x), zip(list1,list2)))
print(out2)