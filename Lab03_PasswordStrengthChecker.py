# Week 3 lab
""" Password Strength Checker with Feedback Loop """
""" This script implements a password strength checker. It evaluates a given password and 
provides real-time feedback and allows users to retry until they create a strong password."""

# below are the integer constant literals
length_threshold = 6
strong_threshold = 15

# below is a list of allowed special characters in password
special_char_list = ['@', '#', '$', '%', '!', '^', '&', '*', '(', ')', '+', '=']

# below are the integer variables
password_len = 0
upper_count = 0
lower_count = 0
special_count = 0
digit_count = 0

# below are the boolean variables
upper_present = False
lower_present = False
special_present = False
digit_present = False
threshold_present = False

# below is a list variable, to store the character categories from password
character_category = []

# below is a dictionary variable, to store the history of passwords along with their respective character categories
password_history = {}

# string variable for password
password_string = str(input(f"Enter the password. It should contain minimum of {length_threshold} characters, combination of upper and lower case alphabets, digits and special characters - {special_char_list}: "))

# while loop to check all passwords entered until at least medium strength password is entered.
while (not threshold_present or not upper_present or not lower_present or not digit_present or not special_present):
    password_len = len(password_string)
    if password_len >= length_threshold:
        threshold_present = True
        character_category = []

        upper_count = 0
        lower_count = 0
        special_count = 0
        digit_count = 0

        upper_present = False
        lower_present = False
        special_present = False
        digit_present = False

        for password_char in password_string:
            if password_char.isupper():
                upper_count += 1
            elif password_char.islower():
                lower_count += 1
            elif password_char.isdigit():
                digit_count += 1
            elif special_char_list.count(password_char) > 0:
                special_count += 1
    
        if upper_count:
            upper_present = True
            character_category.append('upper')
        if lower_count:
            lower_present = True
            character_category.append('lower')
        if digit_count:
            digit_present = True
            character_category.append('digit')
        if special_count:
            special_present = True
            character_category.append('special')

        password_history[password_string] = character_category
        if (not upper_present or not lower_present or not digit_present or not special_present):
            password_string = str(input(f"Weak password. Include character categories like upper and lower alphabets, digits and special characters; try again."))
    else:
        password_string = str(input(f"Weak password. Keep the minimum length of {length_threshold} characters; try again."))
if (threshold_present and password_len < strong_threshold and upper_present and lower_present and digit_present and special_present):
    print("Medium password. Try increasing the length and adding more special characters.")
elif (threshold_present and password_len > strong_threshold and upper_present and lower_present and digit_present and special_present):
    print("Strong password! Great Job!")

# Print the history of all passwords greater than minimum threshold length
print("Here is the history of passwords entered:\n", password_history)
