# import 

import functions_exercises
functions_exercises.some_word('cool')

# use from to import the function directly
from functions_exercises import is_consonant
functions_exercises.is_consonant('jack')

# use from and give the function a different name
from functions_exercises import is_two as double_check
double_check(3)

import json
json.load(open('profiles.json'))

profiles = json.load(open('profiles.json'))




