f = open("practice.txt", "w")
data = ["I like python",'\ni like java']
data = f.writelines(data)
f.close()
