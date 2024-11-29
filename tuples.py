# tuple is similar to a list only that its immutable
# The parentheses are optional, however, it is a good practice to use them.
units = "DAA", "Automata", "Research", "Distributed Systems","HCI", 8.0, 72, "Research" 
print(units)
print(type(units))

# we also use index to access the tuple elements
print(units[1]) # second element
print(units[-1]) # last element

# Tuple methods : count(), index()
print(units.count("Research")) # counts total number of occurence of 'Research' in units
print(units.index("Automata")) # returns the index of the first occurence of Automata