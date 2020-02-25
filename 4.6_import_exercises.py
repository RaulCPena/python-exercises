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
# How many different ways can you combine the letters from 
# "abc" with the numbers 1, 2, and 3?
import itertools as it 

list(it.product([1, 2, 3], 'abc'))

# How many different ways can you combine 
# two of the letters from "abcd"?

# Total number of users
len(profiles)

# Number of active users
len([profile for profile in profiles if profile['isActive']])

# Number of inactive users
len([profile for profile profiles if not profile['isActive']])

# Grand total of balances for all users
def get_profile_balance(profile):
    return float(profile['balance'].replace('$', '').replace(',', ''))

sum([get_profile_balance(profile) for profile in profiles])

# Average balance per user
balances = [get_profile_balance(profile) for profile in profiles]

avg_balance = sum(balances) / len(balances)
print('The average balance is %.2f' % avg_balance)
print('The average balance is {:,.2f}'.format(avg_balance))
print(f'The average balance is {avg_balance:,.2f}')

# User with the lowest balance
user_with_lowest_balance = profiles[0]
for user in profiles[1:]:
    if get_profile_balance(user) < get_profile_balance(user_with_lowest_balance):
        user_with_lowest_balance = user
user_with_lowest_balance

# in order to sort dictionaries, we need to tell python how to compare them
# the key keyword argument specifies a function that takes in one element of the list
# and returns a value that can be sorted
min(profiles, key=get_profile_balance)['name']

# User with the highest balance
max(profiles, key=get_profile_balance)['name']

# Most common favorite fruit

# Least most common favorite fruit
favorite_fruits = [p['favoriteFruit'] for p in profiles]
fruit_counts = {}
for fruit in favorite_fruits:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1
fruit_counts

# other options using the python standard library:
#   - Counter
#   - defaultdict

# Total number of unread messages for all users
[profile['greeting'][-19:-17].strip() for profile in profiles]

def get_n_unread_messages(profile):
    greeting = profile['greeting']
    start_index = greeting.index('have ') + 5
    end_index = greeting.index(' unread')
    return int(greeting[start_index:end_index])

sum([get_n_unread_messages(profile) for profile in profiles])

profile = profiles[0]
greeting = profile['greeting']
int(''.join([c for c in greeting if c.isdigit()]))



