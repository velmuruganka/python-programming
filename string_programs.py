# String Programs

# 1. Reverse a string
text = "PYTHON"
reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]

print("Original:", text)
print("Reverse:", reverse)

# 2. Find length of a string
text = "Programming"
print("Length:", len(text))

# 3. Count vowels
text = "education"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# 4. Check palindrome
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
