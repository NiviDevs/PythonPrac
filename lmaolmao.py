p = 10
q = 10
st = 'loda'
for i in range(1,p+1):
    if i == 1 or i == p:
        print(st * q)
    else:
        print(st + ' ' *(len(st)*(q-2)) + st)