# Variables are container for storing data.
x = 5  # x is integer type
y = 10
z = x + y
print("Sum ", z)

# type
name = "Hamidul"
print(type(name))

# Many Values to Multiple Variables
a, b, c = "Orange", "Banna", "Cherry"
print(a)
# One Value to Multiple Variables
d = e = f = "Orange"
print(e)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
g, h, i = fruits
print(i)

# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
test = "awesome"


def myfun():
    print("Python is " + test)


myfun()
# If you create a variable with the same name inside a function, this variable will be local


def myfun():
    test = "fantastic"  # Local variable
    print("Python is " + test)


myfun()
print("Python is " + test)
