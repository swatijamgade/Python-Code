
# #Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
previous_num = 0
for i in range(0, 10):
    sum = previous_num + i
    print(f"{i} + {previous_num} = {sum}")
    previous_num = i

    
# Write a program to accept a string from the user and display characters that are present at an even index number.
#  Given: I am Learning Python
string = "I am Learning Python"
for i in string[::2]:
    print(i)

#  Check if the first and last number of a list is the same
list1 = [10, 20, 30, 40, 10]
list2 = [75, 65, 35, 75, 30]

if list1[0] == list1[-1]:
    print("first and last number of a list is the same")
else:
    print("first and last number of a list is not the same")

if list2[0] == list2[-1]:
     print("first and last number of a list is the same")
else:
    print("first and last number of a list is not the same")

# Write a program to check if the given number is a palindrome number.
# palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
a = 454
if str(a) == str(a)[::-1]:
    print("This number is pelidrom") 
else:  
    print("yes given number is not palindrome number")
    
def even_num():
    pass

    

