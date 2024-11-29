#A list is an ordered collection of similar or different types
#  of items separated by commas and enclosed within brackets [ ]
# list data type
languages = ["Python", "Dart", "Web", 23,"php", "java"]
print(languages)

# slicing a list
print(languages[2:4]) # index 2 inclusive while index 4 is exclusive
print(languages[2:]) # returns all the items from index 2 upto the end

# it counts from the end backwards when you use a negative index
print(languages[-2])

# accessing list items using index
print(languages[2])

# append() adds items to the list at the end
languages.append("C++")
print("after appending :",languages)

# extend() method adds all items of one list to another.
careers = ["developer","web designer","data analyst","Administrator"]
languages.extend(careers)
print('The new list after extending:',languages)

# change list items , since python lists are mutable
careers[1] = "technician"
print(careers)

# del() used to remove one or more items from a list
del careers[2] # using index
print(careers)
del careers[-1] # deleting the last item
print(careers)

print(languages)
del languages[0:2] # deleting more than one item
print(languages)

# remove() used to remove one item
languages.remove(23) # remove() method uses list values not the indecies
print(languages)

# reverse method
languages.reverse()
print(languages)

# iterating through list items
for x in languages:
    print(x)

# Python List Comprehension
# a list with each item being increasing by power of 2
numbers = [x * x for x in range(1, 6)]
print(numbers)