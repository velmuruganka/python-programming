# Loop Programs

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 1 to 20
print("Even numbers:")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3. Sum of numbers from 1 to 10
total = 0

for i in range(1, 11):
    total = total + i

print("Sum:", total)

# 4. Multiplication table
num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
