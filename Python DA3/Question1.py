dict1 = {1:1, 2:2} ; print(dict1, "Original dictionary")
dict2 = dict1.copy()
dict2.clear(); print(dict2, "Clear")
print(dict2:=dict1.fromkeys([1, 2, 3, 4, 5], 0))
d=dict1.get(4); print(d, "Get")
print(dict1.items(), "Items")
print(dict1.keys(), "Keys")
print(dict1.setdefault(2, 0), "Setdefault")
print(dict1.values(), "Values")
print(dict1:=dict1.update(({6:6, 7:7})), "Update")

# string1 = 'Python is a versatile langauge'
# print(string1.capitalize())
# print(string1.center(5))
# print(string1.casefold())
# print(string1.count('a'))
# print(string1.endswith('language')) 
# print(string1.find("Py"))
# print('''{a} went to the {b} to 
# learn {c}'''.format(a="Nevedya",b="python lab",c="strings"))
# print(string1.index('a')) #Index of a
# print(string1.replace('Python', 'C++'))
# print(string1.upper()) 
# print(string1:=string1.encode('ansi'))