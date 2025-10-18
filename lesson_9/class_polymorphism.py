class Dog:
    def __init__(self, name):
        self.name = name


    def sound(self):
        print(f"{self.name} says Woof!")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} says Meow!")


class bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} says Chirp!")



dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = bird("chip chip")

for animal in (dog, cat, bird):
    animal.sound()
