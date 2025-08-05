# Example of abstraction using abstract base classes in Python

from abc import ABC, abstractmethod  # Import ABC and abstractmethod

# Abstract base class for Employee
class Employee(ABC):

    # Abstract method to be implemented by subclasses
    @abstractmethod
    def get_salary(self):
        pass

# Subclass representing a full-time employee
class fulltimeemploye(Employee):

    # Constructor to initialize salary
    def __init__(self, salary):
        self.salary = salary

    # Implementation of abstract method
    def get_salary(self):
        print(f"Full-time employee salary: {self.salary}")

# Subclass representing a part-time employee
class parttimeemploye(Employee):

    # Constructor to initialize salary
    def __init__(self, salary):
        self.salary = salary

    # Implementation of abstract method
    def get_salary(self):
        print(f"Part-time employee salary: {self.salary}")

# Creating instances and displaying their salaries
f1 = fulltimeemploye(5000)
f1.get_salary()

p1 = parttimeemploye(3000)
p1.get_salary()