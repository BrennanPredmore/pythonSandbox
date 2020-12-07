# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#CREATE A TUPLE (uses paranthesis instead of square brackets)
fruits = ('Apples', 'Bananas', 'Oranges')

# GET VALUE OF SPECIFIC INDEX
print(fruits[1])

# SINGLE VALUE TUPLES MUST HAVE A TRAILING COMMA TO DESIGNATE THEM AS TUPLE AND NOT A LIST
fruits2 = ('Fruits',)
print(type(fruits2))

# FIND THE LENGTH OF THE TUPLE
print(len(fruits))





# A Set is a collection which is unordered and unindexed. No duplicate members.

# CREATE A SET (always uses curly brackets)
fruits_sets = {'Apples', 'Oranges', 'Mangos'}
print('Apples' in fruits_sets)

# ADD TO SET 
fruits_sets.add('Grape')

# REMOVE FROM THE SET
fruits_sets.remove('Grape')

# CLEAR THE SET
fruits_sets.clear()

print(fruits_sets)