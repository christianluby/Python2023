# import random
# import string

# characters = list(string.ascii_letters + string.digits + "!@#$^&*()")

# def generate_password():
#     password_length = int(input("How long would you like your password to be? "))

#     random.shuffle(characters)

#     password = []

#     for x in range(password_length):
#         password.append(random.choice(characters))

#     random.shuffle(password)

#     password = "".join(password)

#     print(password)

# option = input("Do you want to generate a password? (Yes/No)").lower()

# if option == "Yes":
#     generate_password()

# elif option == "No":
#     print("Program terminated")
#     exit()

# else:
#     print("Invalid input, please try again")

import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No)").lower()  # Convert input to lowercase

if option == "yes":
    generate_password()

elif option == "no":
    print("Program terminated")
    exit()

else:
    print("Invalid input, please try again")
