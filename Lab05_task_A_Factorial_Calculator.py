input_number_string = ''
factorial = 1
input_number = 0
while (input_number_string != 'q'):
    input_number_string = input("Enter a positive integer for its factorial, enter q to exit:\n")
    if len(input_number_string) != 0:
        if input_number_string.lower() == 'q':
            break
        else:
            try:
                input_number = int(input_number_string)
            except ValueError:
                print(f"Invalid input {input_number_string}, try again!")
            except Exception as err:
                print(f"Unexpected {err=} occurred, {type(err)=}.")
            else:
                if input_number < 0:
                    print(f"Invalid input {input_number}, try again!")
                else:
                    for i in range(1, input_number+1, 1):
                        factorial *= i
                    print(f"Factorial of {input_number} is {factorial}.")
                    factorial = 1
                    input_number = 0
                    input_number_string = ''
