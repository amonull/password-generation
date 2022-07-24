#!/usr/bin/python

import random
import sys
import re

charachters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

charachters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

charachter_special = ['/', '*', '+', '.', ',', '!', '"', '\'', '#', '$', '%', '^', '&', '-', '_', '\\', '@', '~', '?', '>', '<', '|', '`', '(', ')', ' ']

# replacers are used to replace one charachter with another
replacers = {
            'a': '4',
            'e': '3',
            'B': '8',
            'b': '6',
            'o': '0',
            'g': '9',
            ' ': '_',
            'c': '(',
            }

def main(password=str(), length=14) -> str:
    """main protion of code where a password is generated or sentence is converted to a password"""

    if password:
        for index, replacable_charachter in enumerate(password):
            for key in replacers.keys():
                if replacable_charachter == key:
                    password = re.sub(f"[+{replacable_charachter}]", replacers[key], password)
        return password
    else:
        for x in range(length):
            # grabs a random charachter from the given letters/special_charachters/numbers
            random_charachter = random.choice(random.choice([charachters, charachters_upper, charachter_special, str(random.randint(0,9))]))
            password += random_charachter
        return password

if __name__ == "__main__":
    user_password = str(input("Please enter a sentence to act as your password or leave empty to generate new password (charachter minimum limit 8 (recommended 14), Is Case Sensitive):\n"))

    # checks if the string is empty
    if user_password:
        # checks if user sentence is more than 8 letters
        if len(user_password) >= 8:
            print(f"\nyour password is: \033[33m{main(password=user_password)}")
        else:
            # the random letters before the \n is the color red in ANSI
            sys.exit("\033[31m\nERROR: senetence not long enough\n")
    else:
        try:
            password_length = int(input("Enter how long you want the password to be (leaving blank or entering a non-numeric value will result in using the default value of 14): "))

            if password_length >= 8 and password_length <= 64:
                # should probably assing main() to a varaible and call that in f string for better readability
                # the random letters before the {} is the color yellow in ANSI
                print(f"your password is: \033[33m{main(length=password_length)}")
            else:
                sys.exit("\033[31m\nERROR: choosen number not in range change to a range from 8-64 or remove if else statement at line 63-68\n")
        except ValueError:
            print(f"your password is: \033[33m{main()}")