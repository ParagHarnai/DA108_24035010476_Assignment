coeffient_a = 0.0
coeffient_b = 0.0
coeffient_c = 0.0
valid_coefficient = False

while not (valid_coefficient):
    try:
        coeffient_a = float(input("Enter coefficient 'a' of quadratic equation: "))
    except ValueError:
        coeffient_a = 0.0
        print("Enter a floating point or decimal point value or a whole integer number for coefficient.")
    except Exception as err:
        coeffient_a = 0.0
        print(f"Unexpected {err=} occurred, {type(err)=}.")
    else:
        valid_coefficient = True

if valid_coefficient:
    valid_coefficient = False

while not (valid_coefficient):
    try:
        coeffient_b = float(input("Enter coefficient 'b' of quadratic equation: "))
    except ValueError:
        coeffient_b = 0.0
        print("Enter a floating point or decimal point value or a whole integer number for coefficient.")
    except Exception as err:
        coeffient_b = 0.0
        print(f"Unexpected {err=} occurred, {type(err)=}.")
    else:
        valid_coefficient = True

if valid_coefficient:
    valid_coefficient = False

while not (valid_coefficient):
    try:
        coeffient_c = float(input("Enter coefficient 'c' of quadratic equation: "))
    except ValueError:
        coeffient_c = 0.0
        print("Enter a floating point or decimal point value or a whole integer number for coefficient.")
    except Exception as err:
        coeffient_c = 0.0
        print(f"Unexpected {err=} occurred, {type(err)=}.")
    else:
        valid_coefficient = True

if valid_coefficient:
    root_1 = ((-1*coeffient_b) + (coeffient_b**2 - 4*coeffient_a*coeffient_c)**(1/2))/(2*coeffient_a)
    root_2 = ((-1*coeffient_b) - (coeffient_b**2 - 4*coeffient_a*coeffient_c)**(1/2))/(2*coeffient_a)
    print(f"Coefficient a: {coeffient_a:> 10.6f}\nCoefficient b: {coeffient_b:> 10.6f}\nCoefficient c: {coeffient_c:> 10.6f}\nRoots:   {root_1:> 10.6f}, {root_2:> 10.6f}")
