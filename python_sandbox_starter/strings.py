# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brennan'
age = 37

# CONCATENATE
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

#F-Strings (SHORT CUT INSTEAD OF CONCAT)
print(f'Hello, my name is {name} and i am {age}')



# String Methods

s = 'hello world'
# CAPITALIZE STRING METHOD
print(s.capitalize())
# LOWER CASE STRING METHOD
print(s.lower())