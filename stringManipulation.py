# a string is a sequence of characters.
string1 = "Python"
 
# Access string characters 
# 1. indexing
print(string1[0]) # prints "p"

# 2. Negative indexing
print(string1[-2]) # Prints 'o'

# slicing
print(string1[0:2]) #prints 'py'

# strings are immutable
# but we can assign a new value to the same variable
text = 'Hello'
print(text)

text = 'Hello World!'
print(text)

# create multiline String
# we triple """ or '''
message = '''
my name is clinton
i like football and 
am a software engineer 
'''
print(message)

# comparison of strings
str1 = "hello, world"
str2 = "hello, world ? hope mko best"
str3 = "hello, world"

print(str1 == str2) # prints false
print(str1 == str3) # prints true

# join one or more scripts
greet = 'hello, '
name = 'jacob'
result = greet + name
print(result)

# iterate through a string
for i in greet:
    print(i)

# length of a string
# we use len()
print(len(greet))

# string membership test
print('n' in 'Clinton') # True
print('p' in 'Clinton') # False
print('n' not in 'Clinton') # False

# convertion of string to upper or lower case
Greet = greet.upper() # to upper case HELLO
print((Greet))

Greet = greet.lower() # back to lower case hello
print((Greet))