# A dictionary is an ordered collection of items stored as key/value pairs.
# Below is a dictionary of some countries and their capital cities.
capitalCity = {
    "Kenya": "Nairobi", 
    "Uganda": "Kampala", 
    "Tanzania": "Dar es Salaam", 
    "Ethiopia": "Addis Ababa"
}
print("Initial Dictionary of Capital Cities:", capitalCity)

# Dictionaries can have keys and values of different data types.
# Example: A dictionary mapping integers to their word representation.
numbers = {
    1: "One", 
    2: "Two", 
    3: "Three", 
    4: "Four"
}
print("Number Dictionary:", numbers)

# Adding a new key-value pair to the dictionary
capitalCity["Japan"] = "Tokyo"
print("Updated Dictionary of Capital Cities:", capitalCity)

# Modifying or deleting items in a dictionary
del numbers[1]  # Deletes the key-value pair with key 1
print("Numbers Dictionary after Deletion:", numbers)

numbers[2] = "two"  # Modifies the value of key 2
print("Numbers Dictionary after Modification:", numbers)

# Accessing values in a dictionary using their keys
# Example: Accessing capital cities
print("Capital of Kenya:", capitalCity["Kenya"])
print("Capital of Uganda:", capitalCity["Uganda"])

# Deleting the entire dictionary (commented out to avoid errors)
# del numbers
# print(numbers)  # This will raise an error if 'numbers' is deleted

# Finding the number of items in a dictionary
dict_length = len(capitalCity)
print("Number of Items in Capital Cities Dictionary:", dict_length)

# Checking if a key exists in the dictionary (membership test)
# Note: The "in" keyword tests for keys only, not values.
print("Is 'Ethiopia' a key in the dictionary?", "Ethiopia" in capitalCity)  # True
print("Is 'Somalia' a key in the dictionary?", "Somalia" in capitalCity)   # False

# Iterating through keys in the dictionary using a loop
print("Keys in Capital Cities Dictionary:")
for key in capitalCity:
    print("Key:", key)
