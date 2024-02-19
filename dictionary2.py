# Write a program to sum all the values of a dictionary
# marks={"m1":92 , "m2":56 , "m3":88 , "m4":97 , "m5":89}
# values = marks.values()
# total = sum(values)
# print(total)

# Write a program to get the maximum and minimum value of dictionary.
# marks={"m1":78 , "m2":89 , "m3":64 , "m4":35 , "m5":71}

# v = marks.values()
# maxi = max(v)
# mini = min(v)
# print(maxi)
# print(mini)

# # Write a program to sort dictionary by values (Ascending/ Descending)
# d={"m1":78 , "m2":89 , "m3":64 , "m4":35 , "m5":71}
# values = sorted(x for x in d.values())
# sorted_keys = []
# for item in values:
#     for key in d:
#         if d[keys] == item:
#             sorted_keys.append(ke  ny) 
exit

# Write a program to print keys and values of dictionary separatly
student = {
	"Name": "Tara",
	"RollNo":130046, 
	"Mark": 458, 
	"Age":16,
	"Gender":"Female",
	"City": "Chennai"
}
keylist =[key for key in student]
print(keylist)

# Write a Python program to Rename keys of a dictionary
# student = {
# 	"Name": "Tara",
# 	"RollNo":130046, 
# }
student["name1"] = student.pop("Name")
student["rOLL"] = student.pop("RollNo")
print(student)

# Write a Python program to Delete a list of keys from a dictionary
# keys_to_remove = ["City","Gender"]

# Given - 
student = {
	"Name": "Tara",
	"RollNo":130046, 
	"Mark": 458, 
	"Age":16,
	"Gender":"Female",
	"City": "Chennai"
}

del student["Gender"]
del student["City"]
print(student)

# Drop empty (None) Items from a given Dictionary
student = {"Name": "Pooja", "Age":23, "Gender": None, "Mark":488, "City": None}
del student["Gender"]
print(student)


