class FastFood:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

    def update_price(self, new_price):
        self.price = new_price

    def update_availability(self, availability_status):
        self.availability = availability_status

    def display_info(self):
        print(f"Item: {self.name}")
        print(f"Price: ${self.price}")
        print("Available" if self.availability else "Not Available")
        print()


def add_item(menu, name, price, availability):
    item = FastFood(name, price, availability)
    menu[name] = item
    print(f"{name} added to the menu.\n")


def remove_item(menu, name):
    if name in menu:
        del menu[name]
        print(f"{name} removed from the menu.\n")
    else:
        print(f"{name} is not in the menu.\n")


def update_price(menu, name, new_price):
    if name in menu:
        menu[name].update_price(new_price)
        print(f"{name} price updated.\n")
    else:
        print(f"{name} is not in the menu.\n")


def update_availability(menu, name, availability_status):
    if name in menu:
        menu[name].update_availability(availability_status)
        print(f"{name} availability updated.\n")
    else:
        print(f"{name} is not in the menu.\n")


def display_menu(menu):
    print("---- Menu ----")
    for item in menu.values():
        item.display_info()


menu = {}

add_item(menu, "Chicken Rice", 89.99, True)
add_item(menu, "Noodles", 69.99, True)
add_item(menu, "Parotta", 39.99, False)

display_menu(menu)

update_price(menu, "Chicken Rice", 6.99)

update_availability(menu, "Parotta", True)

remove_item(menu, "Noodles")

display_menu(menu)

   
""" 
OUTPUT:
Chicken Rice added to the menu.

Noodles added to the menu.

Parotta added to the menu.

---- Menu ----
Item: Chicken Rice
Price: $89.99
Available

Item: Noodles
Price: $69.99
Available

Item: Parotta
Price: $39.99
Not Available

Chicken Rice price updated.

Parotta availability updated.

Noodles removed from the menu.

---- Menu ----
Item: Chicken Rice
Price: $6.99
Available

Item: Parotta
Price: $39.99
Available
"""



def calculate_total_cost(quantity, unit_price):
    total_cost = quantity * unit_price
    return total_cost

quantity = 10
unit_price = 25
total_cost = calculate_total_cost(quantity, unit_price)
print("Total cost: $", total_cost)

def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = 48
result = check_even_or_odd(number)
print(number, "is", result)

def find_max_number(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

numbers = [3,21,30,27]
max_number = find_max_number(numbers)
print("Maximum number in list:", max_number)

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

word = "appa" or "amma"
if is_palindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
    
    
"""
OUTPUT:
 Total cost: $ 250
48 is Even
Maximum number in list: 30
appa is a palindrome
"""



def calculate_total_marks(student_marks):
    total_marks = sum(student_marks)
    return total_marks

student_marks = [80, 75, 90, 85, 95]
total_marks = calculate_total_marks(student_marks)
print("Total marks of students:", total_marks)

def get_student_details(student):
    roll_number, name, grade = student
    return f"Roll Number: {roll_number}, Name: {name}, Grade: {grade}"

student = (3004, 'Bhuvi', 'A')
student_details = get_student_details(student)
print(student_details)
student = (3025, 'Theanu', 'A')
student_details = get_student_details(student)
print(student_details)

def check_course_offered(courses, course_name):
    if course_name in courses:
        return True
    else:
        return False

courses = {'DL': 'AD3501', 'D&IS': 'Cw3551', 'BDA': 'ccs334'}
course_name = 'D&IS'
is_offered = check_course_offered(courses, course_name)
if is_offered:
    print(f"{course_name} is offered.")
else:
    print(f"{course_name} is not offered.")

def find_common_interests(student1_interests, student2_interests):
    common_interests = student1_interests.intersection(student2_interests)
    return common_interests

student1_interests = {'Coding', 'Debugging', 'Software Engineer'}
student2_interests = {'Analyst', 'Software Engineer', 'Coding'}
common_interests = find_common_interests(student1_interests, student2_interests)
print("Common interests between students:", common_interests)


"""
OUTPUT:
Total marks of students: 425
Roll Number: 3004, Name: Bhuvi, Grade: A
Roll Number: 3025, Name: Theanu, Grade: A
D&IS is offered.
Common interests between students: {'Software Engineer', 'Coding'}
"""



import datetime

def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

import random

def generate_application_number():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=25))

def check_eligibility(entrance_exam_score, minimum_score):
    if entrance_exam_score >= minimum_score:
        return "Congratulations! You are eligible for admission."
    else:
        return "Sorry, you did not meet the minimum eligibility criteria for admission."

import math

def calculate_scholarship(percentage):
    if percentage >= 90:
        return "Full scholarship"
    elif 80 <= percentage < 90:
        return "50% scholarship"
    else:
        return "No scholarship"

birth_date = datetime.date(2002, 5, 15)
entrance_exam_score = 90
minimum_score = 85
percentage = 95.7

age = calculate_age(birth_date)
application_number = generate_application_number()
eligibility_status = check_eligibility(entrance_exam_score, minimum_score)
scholarship_amount = calculate_scholarship(percentage)

print(f"Age: {age}")
print(f"Application Number: {application_number}")
print(f"Eligibility Status: {eligibility_status}")
print(f"Scholarship Amount: {scholarship_amount}")


"""
OUTPUT:
Age: 21
Application Number: 2VDPN2VFBBEKNGRJTRYG4248O
Eligibility Status: Congratulations! You are eligible for admission.
Scholarship Amount: Full scholarship
"""


