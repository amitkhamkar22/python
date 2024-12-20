"""
In a file called fuel.py, implement a program that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage
rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

/workspaces/76134826/extensionsIf, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError
or ZeroDivisionError.
"""

import operator # import operator helps perform devision (operator.truediv(number))
while True:
    gas = input("Fraction: ").strip().lower()

    num = den = 0

    if "/" in gas:
        num, den = gas.split("/")
    else:
        pass

    try:
        num = int(num)
        den = int(den)

        if num <= den:
            if round(operator.truediv(num,den)*100) >= 99:
                print("F")
                break
            if round(operator.truediv(num,den)*100) <= 1:
                print("E")
                break
            print(f"{round(operator.truediv(num,den)*100)}%")
            break

    except ZeroDivisionError:
        pass

    except ValueError:
        pass