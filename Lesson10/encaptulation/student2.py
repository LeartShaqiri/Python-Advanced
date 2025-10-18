class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


# Creating an object
student1 = Student(name="Orges", age=21)

# Accessing data using properties
print("Name:", student1.name)
print("Age:", student1.age)

# Modifying data using properties
student1.name = "Leart"
student1.age = 16

print("\nUpdated info:")
print("Name:", student1.name)
print("Age:", student1.age)


student1 = Student("Bill", 22)

print("\nStudent Name:", student1.name)
student1.name = "Steve"
print("Updated Student Name:", student1.name)

print("Student Age:", student1.age)
student1.age = 23
print("Updated Student Age:", student1.age)
