class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print(f"I am {self.age} years old.")
    def play(self):
        print(f"{self.name} is playing at the age of {self.age}.")

if __name__ == "__main__":
    parent = Parent("Alice")
    parent.greet()

    child = Child("Bob", 10)
    child.greet()
    child.play()

    print("\nDemonstrating method overriding:")
    child.greet() 