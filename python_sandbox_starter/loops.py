# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['john', 'sarah', 'emma', 'brennan']

#SIMPLE FOR LOOP
# for person in people:
#     print(f'Curent Person {person}')


#BREAK 
# for person in people:
#     if person == 'sarah':
#         break
#     print(f'Curent Person {person}')


#CONTINUE
# for person in people:
#     if person == 'sarah':
#         continue
#     print(f'Curent Person {person}')

# RANGE (MOST SIMILIAR TO JAVASCRIPT FOR LOOP)
# for i in range(len(people)):
#     print(people[i])

# While loops execute a set of statements as long as a condition is true.

count = 0 
while count <= 10:
    print(f'Count {count}')
    count += 1
