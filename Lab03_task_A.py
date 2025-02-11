# Lab 03 Task 01
user_input_string = ''
while (user_input_string != 'q'):
    user_input_string = str(input("user input: "))
    if (user_input_string == 'q'):
        break
    case_altered_string = user_input_string.swapcase()
    print("case altered: ", case_altered_string)
