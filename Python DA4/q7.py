#since these numbers repeat every 35 numbers and 1505 is the first number that satisfies the condition, a simple range function from 1505 to 2701 should do the job
lis = []
for i in range(1505,2700+1,35):
    lis.append(i)
print(lis)