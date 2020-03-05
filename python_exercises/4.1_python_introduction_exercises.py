user_choice = input("Enter an odd integer between 1 and 50: ")
while (user_choice.isdigit() == False # keep prompting user if input is not a whole number
      or int(user_choice) < 1 # prompt if they input less than 1
      or int(user_choice) > 50 # prompt if input greater than 50
      or int(user_choice) % 2 == 0): # prompt if input an even number
    print(f"{user_choice} is nice, but we'll need an odd number between 1 and 50: ")
    user_choice = input("Please input an odd number between 1 and 50: ")
print(f"Number to skip: {user_choice}")

for n in range(1,50):
    if n % 2 != 0:
      if n == user_choice:
        continue
      else:
        print(f"Here is an odd number: {n}")
    
    