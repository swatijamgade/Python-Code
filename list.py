#  Reverse a given list in Python
list1 = [100, 200, 300, 400, 500]

def reverse(list1):
    new_list = list1[::-1]
    return new_list
print(reverse(list1))

# Turn every item of a list into its square. Given a list of numbers. write a program to turn every item of a list into its square.
old = [1, 2, 3, 4, 5, 6, 7]

def square(number):
      return number**2
new = list(map(square, old))
print(new)

#  Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
def remove_empty_strings(string):
    return string != ""
filtered_list = filter(remove_empty_strings, list1)
print(list(filtered_list))
 
#  Add a new item to the list after a specified item. Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
a = 6000
b = 7000

if a in list1:
    list1.append(b)        
else:
    for i in list1:
        if type(i) == list:
            if a in i:
                i.append(b)
                break
            else:
                for j in i:
                    if type(j) == list:
                        if a in j:
                            j.append(b)
                            break
                   
print(list1)

# Extend the nested list by adding the sublist. You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
a =  ["f", "g"]
b = ["h", "i", "j"]

if a in list1:
    a.append(b)
else:
    for i in list1:
        if type(i) == list:
             if a in i:
                i.append(b)
                break
             else:
                 for j in i:
                     if type(j) == list:
                         if a in j:
                             j.append(b)
                             break 
                     else:
                         for k in i:
                            if type(k) == list:
                                if a in k:
                                  k.append(b)
                                  break
                        
print(list1)          

# Calculate the length of a given list
list1 = [x for x in range(50)]       
list = len(list1)
print(list)

# Create a list of all even numbers between 1 and 100 using list comprehension.
for x in range(100):
  if x % 2:
    print(x)

# Concatenate two lists index-wise. Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result=[]
for i in range(0, len(list1)):
    result.append(list1[i]+ list2[i])
print(result)

# Write a program to sum all the elements of a list.
list1 = [2,3,2,4,7,8]
def sumlist(list):
    sum=0
    for i in range(len(list)):
        sum = sum+list[i]
    return sum
list = [10, 9, 7, 5]
print(list)
print("sum of list: ",sumlist(list))

# Write a program to get the maximum number from a list.
list1 = [2,3,2,4,7,8]
list2 = list1[-1]
print(list2)

# Write a program to append data of the second list to the first list. 
# Output:
# [23, 24, 25, 26, 27, 28, 29, 30]
list1 = [23, 24, 25, 26] 
list2 = [27, 28, 29, 30]

list1.append(list2)
print(list1)

# different method
list1.extend(list2)
print(list1)

# different method
result = list1 + list2
print(result)

# Write a program in Python to filter odd and even number from a list.
# Output:
# Even [2, 24, 46] 
# Odd [23, 51, 67]

list1 = [10, 21, 4, 45, 66, 93, 1]
even_count = []
odd_count = []
for num in list1:
    if num % 2 == 0:
        even_count.append(num)
    else:
        odd_count.append(num)
print("Even numbers in the list: ", even_count, len(even_count))
print("Odd numbers in the list: ", odd_count, len(odd_count))