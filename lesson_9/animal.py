class Animal: 
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")



animal = Animal()
animal.sound()  # Output: Some generic animal sound

dog = Dog()
dog.sound()     # Output: Woof!

cat = Cat()
cat.sound()     # Output: Meow!