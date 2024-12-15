def permutations(lst):
    if len(lst) == 1:
        return [lst]
    permutations = []
    for i, elem in enumerate(lst):
        rest = lst[:i] + lst[i+1:]
        for p in permutations(rest):
            permutations.append([elem] + p)
    return permutations

def sum_nested(lst):
    if not lst:
        return 0
    if isinstance(lst[0], list):
        return sum_nested(lst[0]) + sum_nested(lst[1:])
    else:
        return lst[0] + sum_nested(lst[1:])