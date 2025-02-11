temperature = 0.0
celcius_temperature = 0.0
fahrenheit_temperature = 0.0

input_string = ''
input_list = []
celcius_unit = 'Celcius'
fahrenheit_unit = 'Fahrenheit'

while input_string != 'q':
    input_string = str(input(f"Enter the temperature, followed by a space and its unit {celcius_unit} or {fahrenheit_unit}, enter 'q' to exit: "))
    if input_string != 'q':
        input_list = input_string.split(" ")
        try:
            temperature = float(input_list[0])
        except ValueError:
            print(f"Invalid temperature value {input_list[0]}, please enter a number, try again!")
        except Exception as err:
            print(f"Invalid temperature value, unexpected {err=} of {type(err)=} occurred.")
        else:
            if input_list[1].strip()[0].upper() == celcius_unit[0]:
                fahrenheit_temperature = temperature*9/5 + 32
                print(f"Temperature entered  : {temperature:>5.4f} {input_list[1].strip()}.")
                print(f"Temperature converted: {fahrenheit_temperature:>54 c.4f} {fahrenheit_unit}.")
            elif input_list[1].strip()[0].upper() == fahrenheit_unit[0]:
                celcius_temperature = (temperature - 32)*5/9
                print(f"Temperature entered: {temperature:0.4f} {input_list[1].strip()}.")
                print(f"Temperature converted: {celcius_temperature:0.4f} {celcius_unit}.")
