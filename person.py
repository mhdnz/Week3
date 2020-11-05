class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


def people_sort(persons, sort_attr: str):
    for i in range(len(persons)):
        for j in range(i+1, len(persons)):
            if persons[i].__getattribute__(sort_attr) > persons[j].__getattribute__(sort_attr):
                temp = persons[j]
                persons[j] = persons[i]
                persons[i] = temp

    for i in range(len(persons)):
        if i < len(persons)-1:
            print(persons[i].__getattribute__(sort_attr), end=', ')
        else:
            print(persons[i].__getattribute__(sort_attr))


p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

people_sort([p1, p2, p3], "firstname")
people_sort([p1, p2, p3], "lastname")
people_sort([p1, p2, p3], "age")