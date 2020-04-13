
class Employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@yahoo.com"


    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp1 = Employee("Mario", "Del Monaco", 85000)
emp2 = Employee("John", "Doe", 45000)

print(emp1.email)
print(emp2.email)
print(emp1.fullname())

