# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. 
#SIMILIAR TO A JSON OBJECT WITH KEYS


#CREATE DICTIONARY

person = {
    'first_Name': 'John',
    'last_Name': 'Doe',
    'age': 30
}
# print(person, type(person))


# TARGET SPECFIC KEY
# print(person['first_Name'])

# ADD A KEY/VALUE
person['phone'] = '555-555-5555'

# REMOVE AN ITEM
del(person['age'])
#OR
person.pop('phone')


# GET DICTIONARY KEYS
# print(person.keys())
# # GET DICTIONARY ITEMS
# print(person.items())


# COPY DICT
person2 = person.copy()
person2['city'] = 'Austin'

# CLEAR DICTIONARY
person.clear()

# GET LENGTH
# print(len(person2))


# LIST(ARRAY) OF DICTIONARIES
people = [
    {'name': 'Brennan', 'age': 29},
    {'name': 'Emma', 'age': 26}
]

print(people[1]['age'])
# print(person)
# print(person2)