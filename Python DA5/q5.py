from array import * 
arr1 = array("i", list(map(int, input("Enter values: ").split())))
arreve = array('i', filter(lambda x:x%2==0, arr1))
print(arreve)
arrodd = array("i", filter(lambda x: x % 2 != 0, arr1))
print(arrodd)
