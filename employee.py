class Employee(object):
    """ Class for employee"""

    def __init__(self, first_name: str, last_name: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @staticmethod
    def from_string(employee_string: str):
        first_name, last_name, salary = employee_string.split('-')
        return Employee(first_name, last_name, salary)


if __name__ == '__main__':
    emp1 = Employee("Mary", "Sue", 60000)
    emp2 = Employee.from_string("John-Smith-55000")

    print(emp1.first_name)
    print(emp1.salary)
    print(emp2.first_name)
    print(emp2.salary)
