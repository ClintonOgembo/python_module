# A set is a collection of unique data. That is, elements of a set cannot be duplicated
my_set = {227, 228, 229, 230, 232, 227, 233, 233}
print("Student ID: ",my_set) # prints no duplicates

# set of mixed data types
mixed_set = {"Hello", 8, 3.142, -4, "Bye"}
print(mixed_set) # you might get output in a different order. This is because the set has no particular order.

# create an empty set 
# we use set() function because if we use empty{} we will create a dictionary
empty_set = set()

# create empty dictionary
empty_dictionary = { }

print("This is an empty set: ", type(empty_set))
print("This is an empty dictionary: ", type(empty_dictionary))

# sets are mutable, since they are unordered, indexing has no meaning

# add items to a set
my_set.add(234)
print("Updated set: ", my_set)

# Update python set with other collection types (tuples,sets)
companies = {"Lacoste", "Microsoft"}
tech_companies = {"apple", "google","apple"}
companies.update(tech_companies)
print(companies)

# we use discard() method to remove the specified element from a set
removedValue = companies.discard("apple")
print("set after remove(): ",companies)

# len()
length = len(companies)
print(length)
print('Using len() in the print function: ',len(companies))
# max()
maxValue = max(my_set) 
print('maximu value: ',maxValue)
#sorted
sortedSet = sorted(my_set)
print('Sorted set: ',sortedSet)

# sum()
sumOfValues = sum(my_set)
print('Sum of the values in the set: ',sumOfValues)

# all()
allSet = all(my_set)
print(allSet) # returns true if all elements are true/ if the set is empty
# any()
anyset = any(my_set)
print(anyset) # returns true if any element of the set is true. if the set is empty, returns false

# iteration
for i in my_set:
    print('iteration:', i)

# SETS OPERATIONS: (union,intersection,difference)



