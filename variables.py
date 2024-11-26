site_name = "Power Learn Project"
print(site_name)

# Assigning new value to site_name
site_name = "I love coding 😊"
print(site_name)

# Assigning multiple values to multiple variables
a,b,c = 4, 8, "Hello world"
print(a) # prints 4
print(b) # prints 8
print(c) # prints Hello World

# python is case sensitive
num = 88
Num = 510
print(num) #88
print(Num) #510

# use the type() function to know which class a variable or a value belongs to.
print(type(num))

#A list is an ordered collection of similar or different types
#  of items separated by commas and enclosed within brackets [ ]
# list data type
languages = ["Python", "Dart", "Web", 23]
print(languages)

# accessing list items using index
print(languages[2])

#Tuples
#A tuple is an ordered sequence of items same as a list. 
# The only difference is that tuples are immutable. 
# Tuples once created cannot be modified.
products = ('lotion',34.4,'Shoes',21)
print(products)

#SETS:
#The Set is an unordered collection of unique items.
# Set is defined by values separated by commas inside braces { }
student_regno = {55, 127, 221}
print(student_regno)

# Dictionary
# dictionary is an ordered collection of items.
# It stores elements in key/value pairs.
capital_city = {"Kenya": "Nairobi", "Nigeria": "Lagos", "Ethiopia": "Adis Ababa"}
print(capital_city)