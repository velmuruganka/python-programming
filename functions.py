# Function Programs

# 1. Function to add two numbers
def add(a, b):
    return a + b


result = add(10, 20)
print("Addition:", result)


# 2. Function to find square
def square(num):
    return num * num


print("Square:", square(5))


# 3. Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(10))


# 4. Function to find factorial
def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result = result * i

    return result


print("Factorial:", factorial(5))
