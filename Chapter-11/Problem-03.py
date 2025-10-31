# 3. Create a class ‘Employee’ and add salary and increment properties to it.
class Employee:
    salary = 1000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)
    
    @salaryAfterIncrement.setter 
    def salaryAfterIncrement(self,salary):
        self.increment =((salary/self.salary)-1)*100

e = Employee()
e.salaryAfterIncrement = 1200
print(e.salaryAfterIncrement)
print(e.increment)
