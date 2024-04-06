"'create a class, functions with init function '"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Example usage:
person1 = Person("Bhuvi", 20)
person1.introduce()



"'Handle arguments, keyword arguments, default values for the arguments for the function'"

def greet(name, message="Hello"):
  print(f"{message}, {name}!")

greet("Bhuvi")

greet(message="Hi", name="Uma")

greet("Ezhil")



"'Use try, exception in any of the function'"

def safe_division(numerator, denominator):
  try:
    result = numerator / denominator
  except ZeroDivisionError:
    result = "Division by zero is not allowed!"
  return result

result = safe_division(50, 5)
print(result)

result = safe_division(30, 0)
print(result)



"'Use match case in anyone of the function'"


def greet(name, message="Hello"):
    match message:
        case "Hi":
            print(f"Hi, {name}")
        case "Hello":
            print(f"Hello, {name}")
        case "Goodbye":
            print(f"Goodbye, {name}")
        case _:
            print(f"{message}, {name}")

# Call the function with different messages
greet("Bhuvi")
greet("Ezhil", "Hi")
greet("Uma", "Goodbye")
greet("Sarala", "Howdy!")




"""
Hi, my name is Bhuvi and I am 20 years old.
Hello, Bhuvi!
Hi, Uma!
Hello, Ezhil!
10.0
Division by zero is not allowed!
Hello, Bhuvi
Hi, Ezhil
Goodbye, Uma
Howdy!, Sarala
"""