class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def introduce(self):
        return f"Hello, my name is {self.name} and i am {self.age} years old"
    
Person1 = Person("Alice",30)

print("name:", Person1.name)
print("age:", Person1.age)

print(Person1.introduce())
