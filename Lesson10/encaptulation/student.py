class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


# Creating an object
student1 = Student(name="Orges", age=21)

# Accessing data using getters
print("Name:", student1.get_name())
print("Age:", student1.get_age())

# Modifying data using setters
student1.set_name("Leart")
student1.set_age(16)

print("\nUpdated info:")
print("Name:", student1.get_name())
print("Age:", student1.get_age())


student1 = Student(" bill" , 22)

print("Student Name:", student1.get_name())
student1.set_name(" Steve")
print("Updated Student Name:", student1.get_name())

print("Student Age:", student1.get_age())
student1.set_age(23)
print("Updated Student Age:", student1.get_age())