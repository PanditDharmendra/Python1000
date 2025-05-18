dic = {}

for i in range(4):
    key = input("Enter the key: ") # Key as Name.
    value =input("Enter the value: ") #Value as Language
    dic.update({key:value})

print("The required dictionary is: ",dic)
# If the name of two friends are same then what happen.
"If the name of two friends are same then the program take second key:value ."