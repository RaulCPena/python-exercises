# Question 1
# Define a function named is_two. It should accept one input and 
# return True if the passed input is either the number or the 
# string 2, False otherwise.
def is_two (x):
    return x == 2 or x == ('2')

# Question 2
# Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.
def is_vowel(x):
    return len(x) == 1 and x.lower() in 'aeiou'

# Question 3
# Define a function named is_consonant. It should return True if the 
# passed string is a 
# consonant, False otherwise. Use your is_vowel function to accomplish
# this
def is_consonant(x):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return len(x) == 1 and x.lower() in letters and not is_vowel(x)

# Question 4
# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word 
# if the word starts with a consonant.
def some_word(x):
    first = x[0]
    if is_consonant(first):
        return x.title()
    else:
        print(f"{x} does not start with a consonant!")

some_word("btring")

# Question 5
# Define a function named calculate_tip. It should accept a tip 
# percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.
def calculate_tip(price, percent):
    return price * percent

print(calculate_tip(10.5, 0.18))

# Question 6
# Define a function named apply_discount. It should accept a original 
# price, and a 
# discount percentage, and return the price after the discount is 
# applied.

def apply_discount(price, discount):
    return price - (price * discount)

print(apply_discount(13, 0.15))

# Question 7
# Define a function named handle_commas. It should accept a string 
# that is a number that contains commas in it as input, and return 
# Qa number as output.
# Define a function named handle_commas. It should accept a string that is a number that 
# contains commas in it as input, and return a number as output.

def handle_commas(c_string):
    str1 = c_string.replace("," , "")
    str2 = int(str1)
    return str2

print(handle_commas("12,345"))

# Question 8
# Define a function named get_letter_grade. It should accept a number 
# and return the 
# letter grade associated with that number (A-F)

def get_letter_grade(final):
    if final >= 90 and final <= 100:
        return ("You received an A")
    elif final >= 80 and final < 90:
        return ("You received a B")
    elif final >= 70 and final < 80:
        return ("You received a C")
    elif final >= 60 and final < 70:
        return ("You received a D")
    else:
        return ("Sorry, you recieved an F")
print(get_letter_grade(75))

# Question 9
# Define a function named remove_vowels that accepts a string and 
# returns a string with all the vowels removed

def remove_vowels(word):
    new_str = word
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in word.lower():
        if x in vowels:
            new_str = new_str.replace(x, "")
    return new_str

print(remove_vowels("apple"))

    