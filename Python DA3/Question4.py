dict1 = {"c1": "Red", "c2": "Green", "c3": None}
#given
dictcopy = {k:v for k,v in dict1.items() if v}
#generator statement to create the dictionary
print(dictcopy)
