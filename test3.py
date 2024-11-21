def sum_nested(lst):
    if not lst:
        return 0
    if isinstance(lst[0], list):
        return sum_nested(lst[0]) + sum_nested(lst[1:])
    else:
        return lst[0] + sum_nested(lst[1:])

print(sum_nested([1, 2, 3, [1]]))
