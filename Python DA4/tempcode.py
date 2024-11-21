l=[]
charnum = {}
for i in range(9):
    l.append(input())
    charnum[l[i]] = i+1
lnum = int(input())
length = int(input())
def parseToNum(string):
    f=''
    for i in string:
        f+=str(charnum[i])
    return f
def checkInc(num):
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            continue
        else: return False
    return True
def make_combs(comb,length):
    if length==0:
        sval = sum(charnum[i] for i in comb)
        if sval == lnum:
            finale.append(''.join(comb))
        return
    for char in l:
        make_combs(comb + [char],length-1)
        
finale=[]
make_combs([],length)

for i in finale:
    for j in i:
        if i.count(j)>1:
            finale.remove(i)
            break

for k in finale:
    if checkInc(parseToNum(k)):
        print(k)