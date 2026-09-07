# This project is about a Python program that creates a random password for your needs

import random

# Part 1: How many characters should the password contain?
# password_length
while True:
    try:
        password_length = int(input("How many characters should the password contain? "))
        if password_length > 0:
            break
        else:
            print("Please type a number that is bigger than 0")
    except ValueError:
        print("Please type a number! ")


# Part 2: What type of characters should the password contain?
# number, upper_case, lower_case, special_ch

# Function for getting permission
def get_permission(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ["y", "n"]:
            return answer
        else:
            print("Please type either 'y' or 'n'! ")

# Calling the function for each situation
number = get_permission("Would you like the password to contain numbers? (y/n)")
upper_case = get_permission("Would you like the password to contain upper case letters? (y/n)")
lower_case = get_permission("Would you like the password to contain lower case letters? (y/n)")
special_ch = get_permission("Would you like the password to contain special characters? (y/n)")


# Part 3: Building the pool
# nums, lows, ups, specs, pool
nums = "0123456789"
lows = "abcdefghijklmnopqrstuvwxyz"
ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specs = "!@#$%^&*()_+-=[]{}|;:,.<>?"

pool = ""

# Adding into the pool
counter = 0 #How many times does the user say yes?
if number == "y":
    pool += nums
    counter += 1
if upper_case == "y":
    pool += ups
    counter += 1
if lower_case == "y":
    pool += lows
    counter += 1
if special_ch == "y":
    pool += specs
    counter += 1

# What if the number of different types of characters is more than the length of the password?
if counter > password_length:
    print(f"You wanted {password_length} characters, but also ask for {counter} different types of characters?! ")
    exit()

# Controling if the pool is empty (If the user said "n" to all questions)
if len(pool) == 0:
    print("You said no to all questions, terminating process. ")
    exit()


# Part 4: Creating the password.
# temp_password, password

temp_password = []

if number == "y":
    temp_password.append(random.choice(nums))

if upper_case == "y":
    temp_password.append(random.choice(ups))

if lower_case == "y":
    temp_password.append(random.choice(lows))

if special_ch == "y":
    temp_password.append(random.choice(specs))


while len(temp_password) < password_length: # Fill the password to the wanted amount

    temp_password.append(random.choice(pool))

random.shuffle(temp_password) # Shuffle the password for extra security

password = "".join(temp_password)
print("Your password is: ", password)






































