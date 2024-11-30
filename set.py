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
# UNION : all elements in both sets without duplicatess
#We use the | operator or the union() method to perform the set union operation.
A = {1, 3, 5, 2}
B = {0, 2, 4}

# perform union operation using |
print('Union using | : ', A | B)

# perform union operation using union()
print('Union using union() : ', A.union(B))

# INTERSECTION: common elements in both sets
C = {5, 6, 7, 8}
D = {7, 8, 9}
sortedData = sorted(C&D)
print("Intersection using & operator : ", C & D)
print("Intersection using intersection() : ", C.intersection(D))
print("Intersection of sorted elements :", sortedData)

# Difference : of E and F are elements of E that are not in F
E = {2, 3, 5, 7}
F = {1, 3, 5, 11}
print('Difference uning - :', E-F)
print('Difference uning difference() :', E.difference(F))

# Symmetric Difference : All elements in M and N without the common elements
M = {8, 4, 2, 0}
N = {4, 14, 8, 12, 16}
print("Symmetric difference using symmetric_difference : ", M.symmetric_difference(N))
print("Symmetric difference using ^ : ", M ^ N)

# check if two sets are equal
# A and B sets are equal if they have the same number of elements and all elements in set A are in set B and vice versa
# we use == operator 
if M == N:
    print('set M and N are equal')
else:
    print('set M and N are not equal')

# add()
M.add(6)
print(M)

# clear()
M.clear()
print(M)

# copy()
n = N.copy()
print(n)

# pop()
N.pop()
print(N)

# remove()
N.remove(14)
print(N)