from abc import ABC, abstractmethod

# =========================
# Abstract Base Class
# =========================
class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    # Encapsulation with @property
    @property
    def weight(self):
        return self._weight
        

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError("Weight must be positive.")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be positive.")

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self, bmi):
        pass

    @abstractmethod
    def print_info(self):
        pass


# =========================
# Adult Class
# =========================
class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category(bmi)
        print("\n--- Adult Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")

        # Ask for tips
        ask = input("Would you like some tips for your category? (yes/no): ").strip().lower()
        if ask == "yes":
            if category == "Underweight":
                print("\n💡 Tips to gain weight healthily:")
                print("- Eat more frequent meals with nutrient-rich foods.")
                print("- Include healthy fats like nuts, avocados, and olive oil.")
                print("- Drink smoothies or shakes instead of just water.")
            elif category in ["Overweight", "Obese"]:
                print("\n💡 Tips to lose weight safely:")
                print("- Exercise regularly, even simple walks daily.")
                print("- Avoid sugary drinks and processed snacks.")
                print("- Focus on balanced meals with vegetables and lean proteins.")
            elif category == "Normal weight":
                print("\n💡 Tips to maintain your healthy weight:")
                print("- Continue a balanced diet and regular physical activity.")
                print("- Stay hydrated and sleep well.")
        else:
            print("Okay, stay healthy and take care!")


# =========================
# Child Class
# =========================
class Child(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2) *1.3

    def get_bmi_category(self, bmi):
        # Example thresholds (simplified for demonstration)
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 21:
            return "Overweight"
        else:
            return "Obese"

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category(bmi)
        print("\n--- Child Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")

        # Ask for tips
        ask = input("Would you like some tips for your category? (yes/no): ").strip().lower()
        if ask == "yes":
            if category == "Underweight":
                print("\n💡 Tips to gain weight healthily:")
                print("- Eat a variety of foods, including proteins and healthy fats.")
                print("- Have small, frequent meals throughout the day.")
                print("- Drink milk or smoothies to add calories.")
            elif category in ["Overweight", "Obese"]:
                print("\n💡 Tips to stay active and healthy:")
                print("- Play outside or do fun physical activities daily.")
                print("- Eat fruits, vegetables, and home-cooked meals.")
                print("- Avoid too many sweets or soft drinks.")
            elif category == "Normal weight":
                print("\n💡 Keep up the good work!")
                print("- Stay active and eat balanced meals.")
                print("- Avoid too much screen time and get enough sleep.")
        else:
            print("Okay, keep taking care of your health!")


# =========================
# Main Program
# =========================
def main():
    print("=== BMI Calculator ===")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    person.print_info()


if __name__ == "__main__":
    main()


def collect_user_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    return name, age, weight, height




app.BMIapp
app.run()
