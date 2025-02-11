pi = 3.14159
radius_circle = 0.0
area_circle = 0.0
while (True):
    radius_circle_str = str(input("Enter a radius of circle to get area of the circle: "))
    if (radius_circle_str == 'q'):
        break
    try:
        radius_circle = float(radius_circle_str)
    except ValueError:
        radius_circle = 0.0
        area_circle = 0.0
        print("Enter a floating point or decimal point value or a whole positive number for radius.")
    except Exception as err:
        radius_circle = 0.0
        area_circle = 0.0
        print(f"Unexpected {err=} occurred, {type(err)=}.")
    else:
        area_circle = pi*radius_circle**2
        print(f"Radius: {radius_circle:> 10.6f}\nArea:   {area_circle:> 10.6f} square units")
    finally:
        print("Thank you for experimenting!")
