# # Write a program to accept two numbers from the user and calculate multiplication

num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number: "))
def mul(a, b):
    return a * b
print(mul(num1, num2))

# # # Display three string “Name”, “Is”, “James” as “Name**Is**James” using print()
print('my', 'Name',  'Is', 'James' , sep='**')

# # # Write a program to take three names as input from a user in the single input() function call
str1, str2, str3 = input("Enter three string").split()
print("Swati","Ravi","Saee")

# # Accept a list of 5 float numbers as an input from the user
# Output: [78.6, 78.6, 85.3, 1.2, 3.5]

my_list = []
for i in range(5):
    value = float(input("enter values "))
    my_list.append(value)

print(my_list)

# Write a program to use string.format() method to format the following three variables as per the expected output
# Given:
# quantity = 3
# totalMoney = 1000
# price = 450
# Output: I have 1000 dollars so I can buy 3 football for 450.00 dollars.
quantity = 3
totalMoney = 1000
price = 450

msg = "I have {} dollars so I can buy {} football for {} dollars.".format(totalMoney, quantity, price )
print(msg)
# or
msg2 = f"I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars."
print(msg2)