dict1=  {'Animal':700, 'Ball':5874,'Dat': 560,'Dog':400,'Eho':5874, 'Fan': 20}
#given in question
s = sum(dict1.values())
#obtained values then summed it all
largest = max(dict1.values())
#finding largest value
dict1.pop(max(dict1, key=dict1.get))
#removing largest value to make the second largest value the current largest value
second_largest = max(dict1.values())
#finding second largest value
print("Sum of all items in dictionary is : ", s)
print("Two largest values are :", largest, second_largest,  sep='    ')
