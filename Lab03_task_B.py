# Lab 03 Task 02
user_input_string = ''
while (user_input_string != 'q'):
    user_input_string = str(input("user input: "))
    if (user_input_string == 'q'):
        break
    output_string = user_input_string.replace(' ', ' ... ')
    print("output: ", output_string)
