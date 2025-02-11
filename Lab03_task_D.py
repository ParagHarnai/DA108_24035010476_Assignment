# Lab 03 Task 04
user_input_string = ''
user_input_number = 0
while (user_input_string != 'q'):
    user_input_string = str(input("Enter a number to check the number of byte it takes for binary representation in Python: "))
    if (user_input_string == 'q'):
        break
    if not user_input_string:
        continue
    try:
        user_input_number = int(user_input_string)
    except ValueError:
        print(f"{user_input_string} is invalid. Enter an integer number only.")
        user_input_string = ''
        user_input_number = 0
    else:
        user_input_bytes = (user_input_number.bit_length()) // 8 + (((user_input_number.bit_length()) % 8) > 0)
        print(f"user input: {user_input_string:>6}\noutput: {str(user_input_bytes):>10}")
