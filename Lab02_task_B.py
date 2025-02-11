celcius = 0.0
fahrenheit = 0.0
celcius_str = ''
while (True):
    celcius_str = str(input("Enter the temperature in celcius to get its value in fahrenheit: "))
    if (celcius_str == 'q'):
        break
    try:
        celcius = float(celcius_str)
    except ValueError:
        celcius = 0.0
        fahrenheit = 0.0
        print("Enter a floating point or decimal point value or a whole positive number for temperature.")
    except Exception as err:
        celcius = 0.0
        fahrenheit = 0.0
        print(f"Unexpected {err=} occurred, {type(err)=}.")
    else:
        fahrenheit = 9/5*celcius + 32
        print(f"Celcius:    {celcius:> 10.4f}\nFahrenheit: {fahrenheit:> 10.4f}")
    finally:
        print("Thank you for experimenting!")
