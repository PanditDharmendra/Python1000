# . Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin, ):
        self.name = name
        self.salary = salary
        self.pin = pin

P = Programmer("Dharmendra", 100000, 2233550)
print(P.salary, P.name, P.pin )
R = Programmer("Rohan", 30000, 595955)
print(R.name, R.pin)



