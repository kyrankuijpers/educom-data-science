class Person:
    def __init__(self, name: str, age: int, city: str, id: int | None = None):
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        