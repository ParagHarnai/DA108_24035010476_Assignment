import random

guess_number_response = 'y'
guess_number_string = ''
guess_number = -1
guess_history = []
random_number = 0

while (guess_number_response.lower != 'n'):
    guess_number_response = input("System will generate a random number between 0 and 100 and you need to guess it, ready to play? Enter y to proceed or n to exit: ")
    if guess_number_response:
        if (guess_number_response[0].lower() == 'y'):
            random_number = random.randint(0, 100)
            while guess_number_string.lower() != 'q':
                guess_number_string = input("Enter your guess between 0 and 100 to proceed or q to exit: ")
                if len(guess_number_string) != 0:
                    if guess_number_string.lower() == 'q':
                        break
                    else:
                        try:
                            guess_number = int(guess_number_string)
                        except ValueError:
                            print(f"Invalid input {guess_number_string}, try again!")
                        except Exception as err:
                            print(f"Unexpected {err=} occurred, {type(err)=}.")
                            break
                        else:
                            if guess_number < 0:
                                print(f"Invalid input {guess_number}, try again!")
                            else:
                                if abs(guess_number - random_number) > 10:
                                    guess_history.append(guess_number)
                                    print(f"Guess {guess_number} too high, try again!")
                                elif (abs(guess_number - random_number) <= 10) and (abs(guess_number - random_number) > 5):
                                    guess_history.append(guess_number)
                                    print(f"Guess {guess_number} low and closer, keep trying!")
                                else:
                                    guess_history.append(guess_number)
                                    print(f"\nWell done!, your guess this time {guess_number} is very close, please find below the random number and history of your guess attemps:\n")
                                    print(f"{random_number=}, {guess_history=}\n")
                                    break
        elif (guess_number_response[0].lower() == 'n'):
            break
