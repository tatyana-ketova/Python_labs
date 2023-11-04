"""
You are given two variables:

age = 4
name = "Sammy"

Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
"""

age = 4
name = "Sammy"
print("Hello my dogs name is {} and he is {} years old".format(name, age))
print("Hello my dog's name is "+str(name)+"and he is "+str(age)+" years old")