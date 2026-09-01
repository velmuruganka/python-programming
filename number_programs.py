# Number Programs

# 1. Factorial of a number
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial:", factorial)

# 2. Check whether a number is prime
num = 17
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

# 3. Reverse a number
num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

# 4. Sum of digits
num = 1234
total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits:", total)
