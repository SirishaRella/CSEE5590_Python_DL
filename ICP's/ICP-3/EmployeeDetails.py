# Employee class
class Employee:
    countEmployees = 0
    salaries = []

    #Default constructor function
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        #appending salaries to the list
        Employee.salaries.append(self.salary)
        Employee.countEmployees = Employee.countEmployees + 1

    #Average salary of all employess
    def avgsalary(self, salaries):
        length = len(salaries)
        totalsalary = 0
        for salary in salaries:
            totalsalary = totalsalary + salary
        print("Average Salary = ", totalsalary/length)


#Full time Employee class
class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


Employee1 = Employee("siri", "Rella", 1000,"CSE")
FulltimeEmployee1 = FulltimeEmployee("Sourav", "Verma", 2000,"ECE")

print(Employee1.name)
print(FulltimeEmployee1.name)

# Access data member using FulltimeEmployee class
print("Number of Employees: " , Employee.countEmployees)
FulltimeEmployee1.avgsalary(FulltimeEmployee.salaries)

