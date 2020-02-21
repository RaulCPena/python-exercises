# 1. Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not

day = input('What day is it,')
if day == 'Monday':
    print('Yay today is Monday and we are ready for work!')
else:
    print('Come back when it is Monday')

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
prompt = input('What day is it?')
if day in weekday:
    print("Hey, that's a weekday")
else:
    print("It's time to party")

# c. create variables and make up values for

#         - the number of hours worked in one week
#         - the hourly rate
#         - how much the week's paycheck will be
#     write the python code that calculates the weekly paycheck. You get paid time and a half if you work 
#     more than 40 hours

hours = 52
rate = 10
if hours <= 40:
    total = rate * hours
    print("Here is your total for the week is", "$",total)
if hours > 40:
    reg_hours = 40
    over_time_hours = hours - 40
    ot = rate * 1.5
    total_plus_ot = (over_time_hours * rate) + (reg_hours * rate)
    print("You worked overtime so your weeks pay is", "$", + total_plus_ot)

#  While
# Create an integer variable i with a value of 5.
i = 5

# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment 
# i by one.
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and 
# ending at 100. Follow each number with a new line.
i = 0
n = 1000000
while i <= 100:
    print(i)
    i += 2
# Alter your loop to count backwards by 5's from 100 to -10
n = 100
while n >= -10:
    print(n)
    n -= 5

# Create a while loop that starts at 2, and displays the number 
# squared on each line while the number is less than 1,000,000
n = 2
while n <= 1000000:
    print(n)
    n = n ** 2

# Write a loop that uses print to create the output shown below
n = 100
while n >= 5:
    print(n)
    n -= 5

# Write some code that prompts the user for a number, then shows a 
# multiplication table up through 10 for that number.

num = int(input("Display multipliation table of?" ))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

# Create a for loop that uses print to create the output shown below.
# 1 22 333 4444 55555 666666 7777777 88888888 999999999
for i in range(10):
    print(str(i) * i)

# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user 
# if they enter invalid input. (Hint: use the isdigit method on 
# strings to determine this).
user_choice = int(input("Enter an odd integer between 1 and 50: "))
while (str(user_choice).isdigit() == False # keep prompting user if input is not a whole number
      or int(user_choice) < 1 # prompt if they input less than 1
      or int(user_choice) > 50 # prompt if input greater than 50
      or int(user_choice) % 2 == 0): # prompt if input an even number
    print(f"{user_choice} is nice, but we'll need an odd number between 1 and 50: ")
    user_choice = int(input("Please input an odd number between 1 and 50: "))
print(f"Number to skip: {user_choice}")

for n in range(1,50):
    if n % 2 != 0:
      if n == user_choice:
        print(f"Yikes! Skipping number: {n}")
        continue
      else:
        print(f"Here is an odd number: {n}")

# Write a program that prompts the user for a positive 
# integer. Next write a loop that prints out the 
# numbers from the number the user entered down to 1.


# Fizzbuzz

# One of the most common interview questions for entry-level 
# programmers is the FizzBuzz test. Developed by Imran Ghory, 
# the test is designed to test basic looping and conditional 
# logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the 
# number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and 
# five print "FizzBuzz".


# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the 
# value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125


# Bonus

# Edit your grade ranges to include pluses and minuses 
# (ex: 99-100 = A+).


# Create a list of dictionaries where each dictionary 
# represents a book that you have read. Each dictionary 
# in the list should have the keys title, author, and 
# genre. Loop through the list and print out information 
# t each book.

# Prompt the user to enter a genre, then loop through 
# your books list and print out the titles of all the 
# books in that genre.