# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#SAMPLE JSON
# userJSON = '{"first_Name": "Brennan", "last_Name": "Predmore", "age": 29}'

# PARSE TO DICTIONARY
# user = json.loads(userJSON)
# print(user)

car = {'make': 'Ford', 'model': 'Mustand', 'year': 1970}

carJSON = json.dump(car)

print(carJSON)