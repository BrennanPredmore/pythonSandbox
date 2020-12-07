# A List is a collection which is ordered and changeable. Allows duplicate members.
#AKA AN ARRAY


# BOTH OF THESE ARE EXAMPLES OF A LIST

# / CREATE A LIST (most common way)
numbers1 = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#USE A CONSTRUCTOR
number2 = list((1, 2, 3, 4, 5))

print(numbers1, number2)

# GET A VALUE USING INDEX
print(fruits[2])

# GET LENGTH
print(len(fruits))

# APPEND TO LIST
fruits.append('Mangos')

# REMOVE FROM LIST
fruits.remove('Grapes')

#INSERT INTO POSITION
fruits.insert(2, 'Strawberries')

# CHANGE VALUE
fruits[0] = "Blueberries"

# REMOVE WITH POP (remove by index)
fruits.pop(2)

# Reverse List
fruits.reverse()

# Sort list
fruits.sort()

# REVERSE SORT
# fruits.sort(reverse=True)

print(fruits)