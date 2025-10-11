class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound")

    def description(self):
        print(f"This is an animal named {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Woof!")

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Meow!")

    def description(self):
        super().description()
        print(f"Color: {self.color}")



# test 
animal = Animal("Frost")
animal.sound()
animal.description()

frost = Dog("Frost", "Husky")
frost.sound()
frost.description()
