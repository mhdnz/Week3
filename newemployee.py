class NewEmployee:

    def __init__(self, full_name: str, salary: int = 0, height: int = 0, nationality: str = ""):
        self.name, self.last_name = full_name.split(' ')
        self.salary = salary
        self.height = height
        self.nationality = nationality


if __name__ == '__main__':
    john = NewEmployee("John Due")
    mary = NewEmployee("Mary Major", salary=120000)
    richard = NewEmployee("Richard Roe", salary=110000, height=178)
    giancarlo = NewEmployee("Giancarlo Lossi", salary=115000, height=182, nationality="Italian")

    print(john.name)
    print(mary.last_name)
    print(richard.height)
    print(giancarlo.nationality)