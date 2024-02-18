
# Calculate the length of the string.
# input= "ABCDFGH"
# Output: 7

str1 = "ABCDFGH"
print(len(str1))
exit
# # print(ord('A'))
# # print(chr(65))

def findLen(str1):
    counter = 0   
    for i in str1:
        counter += 1
    return counter
str1 = "ABCDFGH"
print(findLen(str1))
exit

# # Create a string made of the first, middle and last character. Write a program to create a new string made of an input string’s first, middle, and last character.
str_name = "Sharvin"

first_char = str_name[0]
middel_char = str_name[int(len(str_name)/2)]
last_char = str_name[-1]   
def string(name):
    first_char = name[0]
    middel_char = name[int(len(name)/2)]
    last_char = name[-1]
    return first_char + middel_char + last_char

modified_char = string(str_name)
print(modified_char)

# Create a string made of the middle three characters. Write a program to create a new string made of the middle three characters of an input string.
# Input: "JhonDipPeta"
# Output: "Dip"

str1 = "JhonDipPeta"
print(str1[int(len(str1) / 2)])

def string(name):
    middle_point = int(len(name) / 2)
    return name[(middle_point-1):(middle_point+2)]

modified_char = string(str1)
print(modified_char)

# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# Input:
# s1 = "Ault"
# s2 = "Kelly"
# Output: "AuKellylt"

def append_middle(s1,s2):
      mi = int(len(s1) / 2)
      x = s1[:mi:]


# Arrange string characters such that lowercase letters should come first. Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Input: IamLearningPython
# Output: amearningpthonILP
      
str1 ="IamLearningPython" 
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_str = ''.join(lower + upper)
print(sorted_str)

    
# Count all letters, digits, and special symbols from a given string
str1 = "I@#am26at^&i5ve"
   
def find_digit_letter_symbol(str1):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in str1:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)      
         
str1 = "P@yn2at&#i5ve"
find_digit_letter_symbol(str1)

# Find all occurrences of a substring in a given string by ignoring the case. Write a program to find all occurrences of “USA” in a given string ignoring the case.
# Input:  "Welcome to USA. usa awesome, isn't it?"
# Output: The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?"
main = "USA"

result = str1.lower()
count = result.count(main.lower())
print(count)

# Reverse a given string
# Input: "IamLearningPython"
# Output: "nohtyPgninraeLmaI"
str1 = "IamLearningPython"

str1 = str1[::-1]
print(str1)
exit

str1 = "PYnative"
str1 = ''.join(reversed(str1))
print(str1)

# Find the last position of a given substring. Write a program to find the last position of a substring “Emma” in a given string.
# Input: "Emma is a data scientist who knows Python. Emma works at google."
# Output: Last occurrence of Emma starts at index 43

str1 = "Emma is a data scientist who knows Python. Emma works at google."
index = str1.rfind("Emma")
print(index)



