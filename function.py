# what up yo!
# greet functions with no arguments
def greet():
    print("Welcome to Feb 2019 Class!")

greet()


def greet_with_name(name):
    print(f"Welcome {name} to Feb 2019 Class!")

def greet_with_name_and_age(name, age):
    print(f"Welcome {name} and your age is {age}")

greet_with_name("Tim")
greet_with_name_and_age('Tim', 39)

# function with optional arguments

def greet_with_opetional_age(name, age = 32):
    print(f'{name} and age is {age}')

greet_with_opetional_age('Tim', 39)
