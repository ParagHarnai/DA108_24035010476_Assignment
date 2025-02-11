input_username = ''

while input_username != 'q':
    input_username = str(input(f"Enter the username to validate, at least 5 characters, no special characters, no spaces allowed, enter 'q' to exit: "))
    if input_username != 'q':
        if (input_username.isalnum() and len(input_username) > 4):
            print(f"Valid username: {input_username}")
        else:
            print(f"Invalid username: {input_username}")
