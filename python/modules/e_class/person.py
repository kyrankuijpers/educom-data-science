class Person:
    def __init__(self, name: str, age: int, city: str, id: int | None = None):
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        
    def to_dict(self):
        object_as_dict = {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "city": self.city
            } 
        return object_as_dict        