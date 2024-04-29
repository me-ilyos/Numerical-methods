from prettytable import PrettyTable
import sympy as sp
import math


def fixed_decimal(value, decimals):
    return f"{value:.{decimals}f}"


def find_root_newton():
    x = sp.Symbol("x")

    while True:
        func_str = input("Funksiyani x ga nisbatan kiriting: ")

        def get_func_from_user():
            f_expr = sp.sympify(func_str)
            f_derivative = sp.diff(f_expr, x)
            f = sp.lambdify(x, f_expr, modules=["math"])

            return f, f_expr, f_derivative

        fx, function_expression, function_derivative = get_func_from_user()

        a, b, error = [
            float(y)
            for y in input(
                "Quyidagilarni kiriting a, b, error (a va b yechimga ega bolishi kerak.): "
            ).split(",")
        ]

        if fx(a) * fx(b) < 0:
            break
        else:
            print("a va b yechimga ega emas. Boshqatdan kiriting.")

    print(f"\n\n(a,b) = [{a}, {b}], error = {error}")
    print(f"***\nFunction derivative: {function_derivative}\n***")

    table = PrettyTable(["n", "x_n", "f(x_n)", "f'(x_n)"])

    n = 0

    c = a - fx(a) * ((b - a) / (fx(a) * fx(b)))
    x_0 = a if fx(a) * fx(c) < 0 else b

    while True:
        n += 1
        fxn_derivative = function_derivative.subs(x, x_0)
        xn = x_0 - (fx(x_0) / fxn_derivative)
        fxn = fx(xn)
        table.add_row(
            [
                n,
                fixed_decimal(xn, 7),
                fixed_decimal(fxn, 7),
                fixed_decimal(fxn_derivative, 7),
            ]
        )

        if abs(xn - x_0) <= error:
            print(table)
            break
        else:
            x_0 = xn


if __name__ == "__main__":
    find_root_newton()
