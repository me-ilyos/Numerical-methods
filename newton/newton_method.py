import sympy as sp
import math

error = 0.001


def function_at_point(x):
    print(f"point x = {x}")
    # return pow(x, 3) - (x * 6) + 4
    # return ((4 - x) + ((x-1)/(x+1) ** 1/3))
    # return (x**3 - math.sin(x))
    return (x - 2 - x**(1/4))


def function_at_point1(a):
    x = sp.Symbol('x')

    # derr1 = sp.diff(x**3 - 6*x + 4, x)

    # derr = sp.diff(((4 - x) + ((x-1)/(x+1) ** 1/3)))

    # derr = sp.diff(x**3 - sp.sin(x))
    derr = sp.diff(x - 2 - x**(1/4))

    print(f"f'(x) = {derr}")

    return derr.subs(x, a)


while True:
    x0 = 0

    a, b = [float(y) for y in input("a, b: ").split(',') ]
    
    if function_at_point(a) * function_at_point(b) < 0:
        c = a - (function_at_point(a) * ((b - a) / (function_at_point(b) - function_at_point(a))))

        if function_at_point(a) * function_at_point(c) < 0:
            x0 = a
        else:
            x0 = b

        while True:

            x = x0 - (function_at_point(x0) / function_at_point1(x0))

            if abs(x - x0) < error:
                print(f"x: {x}")
                break
            else:
                print(f"x: {x}, f(x): {function_at_point(x)}")
                x0 = x
