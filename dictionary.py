# Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def merge(dict_1,dict_2):
    result = dict_1 | dict_2
    return result
dict_1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict_2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict_3 = merge(dict_1,dict_2)
print(dict_3)

eys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


# Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

# Print the value of key ‘history’ from the below dict
sample_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
# sample_dict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sample_dict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sample_dict['class']['student']['marks'] = {'physics': 70, 'history': 80}

print(sample_dict['class']['student']['marks']['history'])

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

Output: {'name': 'Kelly', 'salary': 8000}
    
new_dict = {}

new_dict["name"] = sample_dict.get("name")
new_dict["salary"] = sample_dict.get("salary")
print(new_dict)


#  Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]
# Expected output: {'city': 'New york', 'age': 25}

keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)


#  Write a Python program to check if value 200 exists in the following dictionary.

# sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict:
    print("200 not present in a dict")
else:
    print("200 present in a dict")

# Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)

#  Write a Python program to check if value 200 exists in the following dictionary.

# sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict:
    print("200 not present in a dict")
else:
    print("200 present in a dict")
