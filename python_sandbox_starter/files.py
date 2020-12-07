# Python has functions for creating, reading, updating, and deleting files.

# OPEN FILES (create files)
myFile = open('myFile.txt', 'w')


# GET SOME INFO
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening: ', myFile.mode)

# WRITE TO FILE
myFile.write('I Love python')
myFile.write(' and JavaScript')
myFile.close()

# APPEND TO FILE
myFile = open('myFile.txt', 'a')
myFile.write(' I also like NODE')
myFile.close()

# READ FROM A FILE
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)