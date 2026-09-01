# Conditional Statement Programs

# 1. Check whether a number is positive or negative
num = 10

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# 2. Check whether a number is even or odd
num = 15

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. Find the largest of two numbers
a = 25
b = 40

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

# 4. Check voting eligibility
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
