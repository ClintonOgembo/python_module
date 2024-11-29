# Python dictionary is an ordered collection of items. It stores elements in key/value pairs
capitalCity = {"Kenya" : "Nairobi", "Uganda" : "Kampala", "Tanzania" : "Dar el Salam", "Ethiopia" : "Adis Ababa"}
print(capitalCity)

# we can also have keys of diff data type and values of diff data type
numbers = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
print(numbers)

# Adding elements to a dictionary
capitalCity["Japan"] = "Tokyo"
print("Updated Dictionary: ",capitalCity)

# change values of a dict
del numbers[1] # deleting
print("Update numbers: ", numbers)
numbers[2] = "two" # changing "Two" with "two"
print(numbers)

# accessing elements from a Dict
# we use the keys to access the corresponding values
print(capitalCity["Kenya"]) # prints Nairobi
print(capitalCity["Uganda"]) # prints Kampala

# we can also delete a whole dictionary
# del numbers
# print(numbers)

# length of a dict
dict_length = len(capitalCity)
print(dict_length)

# dictionary membership test
# we use the keyword "in" and we only test the keys not the values
print("Ethiopia" in capitalCity) # returns true
print("Somalia" in capitalCity) # returns false, since the key Somalia does not exist in the dict

# iterating through each key using a loop
for r in capitalCity:
    print('key', r)