input_number_string = ''
prime_number = False
input_number = 0
prime_mod = 0
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
                        prime_mod = input_number % i
                        if ((input_number == 2) or (input_number == 3)):
                            prime_number = True
                            break
                        elif ((i != 1) and (i != input_number) and (not prime_mod)):
                            break
                        elif (i == input_number):
                            prime_number = True
                            break
                        else:
                            continue
                    if prime_number:
                        print(f"{input_number} is prime.")
                        prime_number = False
                    else:
                        print(f"{input_number} is not prime.")
                    prime_mod = 0
                    input_number = 0
                    input_number_string = ''
