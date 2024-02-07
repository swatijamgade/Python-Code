# Write a function that accepts a number and return cube of it.

def cube(n):
    return n**3

result = cube(2)
print(result)

#  Write a Python function called add_numbers that takes two parameters, num1 and num2, and returns the sum of the two numbers.

def add_numbers(num1,num2):
    return num1 + num2
result = add_numbers(2,3)
print(result)

#  Create a function called calculate_area that calculates the area of a rectangle. It should take two parameters: length and width, and return the area.

def calculate_area(length,width):
    return length * width
result = calculate_area(5,3)
print(result)


#  Define a function called check_even that takes an integer as input and returns True if the number is even, otherwise returns False.
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = check_even(2)

print(result)

# Write a function called reverse_string that takes a string as input and returns the reverse of that string

def reverse_string(strpar):
    return strpar[::-1]
result = reverse_string("SWATIPATIL")
print(result)   

# Create a function called find_max that takes a list of numbers as input and returns the maximum number in the list

def find_max (list1):
    # return max(list1)
    maxVal = 0
    for i in range(len(list1))    :
        if maxVal < list1[i]:
            maxVal = list1[i]

    return maxVal

result = find_max([1,2,3,4,15,6,17,8])
print(result)

# Define a function called calculate_factorial that takes an integer as input and returns the factorial of that number.

def calculate_factorial(n): 
    fact = 1
    for i in range(1, n+1):# range(start = 1,end = max number)
        print(i)
        fact = fact * i
    return fact
result = calculate_factorial(4)

print(result)


#  Write a function called is_prime that takes an integer as input and returns True if the number is prime, otherwise returns False.
def isprime(num1):
    if  (num1 != 2 and num1 != 3 and num1 != 5) and (num1 % 2 == 0 or num1 % 3 == 0 or num1 % 5 == 0):  # Condition to check if number is divisible by any number other than same number.
        return False
    else:
        return True

result = isprime(72)
print(result)

# Create a function called count_vowels that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
   
def countvowels(string):
    num_vowels=0

    for char in string:
        if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
           num_vowels = num_vowels + 1
    return num_vowels   
result = countvowels("function")  
print(result)      
#
# Define a function called calculate_average that takes a list of numbers as input and returns the average of those numbers.

def cal_average(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num + i           
    avg = sum_num / len(num)
    return avg              

result = cal_average([10,20])
print(result)
        
#  Write a function called check_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), otherwise returns False.


def isPalindrome(str1):

    if str1.lower() == str1[::-1].lower():
        return True
    else:
        return False
    
result = isPalindrome("Nitin")
print(result)
