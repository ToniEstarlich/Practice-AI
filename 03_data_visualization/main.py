# 1. Class
class Person:

    # 2. Data
    def __init__(self):
        self.name = "Richard"
        self.age = 30

    # 3. Action
    def hello(self):
        print(f"Hello {self.name}")
        print(f" I am {self.age} years old.")
        print("Nice to meet you!")

# 4. Create and use the object
person = Person()
person.hello()