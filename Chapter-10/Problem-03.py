class Myattribute:
    a = 100

obj = Myattribute()
print(obj.a)
print(Myattribute.a)

# Changing the class attribute
obj.a= 110
print("obj.a= ", obj.a)
print("My attribute.a", Myattribute.a)