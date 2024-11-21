tup = [
    ("lucky", "18.265"),
    ("nikhil", "14.107"),
    ("akash", "24.541"),
    ("anand", "4.256"),
    ("gaurav", "10.365"),
]
tup = sorted(tup,key = lambda x : float(x[1]))

print(tup)