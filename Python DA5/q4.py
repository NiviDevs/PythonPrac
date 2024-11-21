from array import *
arr1 = array('i',list(map(int,input("Enter values: ").split())))
avg = sum(arr1)/len(arr1)
arr2 = array('f',list(map(lambda x : avg - x , arr1)))
print("Average: ",avg)
print(arr2)
