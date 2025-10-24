class TowD_Vector:
    studio = "Mud Art"
    def name(self):
        print(f"The name of the stdudio is {self.studio}")

class ThreeD_Vector(TowD_Vector):
    Num = "Y_combinator"
    def Name (self):
        print(f"The name of the studio is {self.Num}")


# e = TowD_Vector()
# e.name()

r = ThreeD_Vector()
# r.Name()
# r.name()
print(r.studio, r.Num)
