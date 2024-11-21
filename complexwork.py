data = ((11, 12), (13, 14, (15, 16)), (17, (18, 19)))

data = list(data)
m = list(data[1])
m.remove(14)
m = tuple(m)
data.insert(1, m)
data.pop(2)
data[2] = (17, (18, 19, 15))
print(tuple(data))

'im seeing how git works lmao'
print(data[2][0])
print(data[2][1][1])


def isIter(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def countNest(tup, ele):
    count = 0
    for i in tup:
        if isIter(i):
            count += countNest(i, ele)
        else:
            if i == ele:
                count += 1

    return count


print(countNest(data, int(input("Enter element to count : "))))


