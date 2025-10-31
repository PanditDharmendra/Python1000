# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def Name(self):
        self.name = "Dharmendra"
        print(f"The name is {self.name}")
        
class Pets(Animals):
    No_animals = 100
    print (f"The No.  of Animals {No_animals}")
    
class Dog(Pets):
    def Bark(self):
        sound = "Bho Bho"
        print(f"The sound of the dog is {sound}")

e = Dog()
# e = Pets()
e.Bark()
e.Name()
print(e.No_animals)