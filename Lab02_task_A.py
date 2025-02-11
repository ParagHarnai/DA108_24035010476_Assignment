import decimal

user_input_mass = '0.0'
speed_of_light = 300000000
while (user_input_mass != 'q'):
# while (True):
    user_input_mass = str(input("Enter the mass of an object in kilogram, to get its energy in Joules: "))
    if (user_input_mass == 'q'):
        break
    try:
        energy = decimal.Decimal(user_input_mass)*(speed_of_light**2)
    except ValueError:
        energy = 0.0
        user_input_mass = '0.0'
        print("Enter a floating point or decimal point value or a whole positive number for mass.")
    except decimal.InvalidOperation:
        energy = 0.0
        user_input_mass = '0.0'
        print("Enter a floating point or decimal point value or a whole positive number for mass.")
    except Exception as err:
        energy = 0.0
        user_input_mass = '0.0'
        print(f"Unexpected {err=} occurred, {type(err)=}.")
    else:
        # print(f"The value of energy is {energy} joules.")
        print(f"Mass: {user_input_mass} Kg\nEnergy: {energy} Joules")
    finally:
        print("Thank you for experimenting!")
