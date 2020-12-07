# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#CORE MODULES
import datetime
from datetime import date
import time
from time import time

#PIP MODULE
import camelcase

# today = datetime.date.today()
today = date.today()
timeStamp = time()

print(timeStamp)