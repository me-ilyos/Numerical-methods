from prettytable import PrettyTable
import sympy as sp
import math


def fixed_decimal(value, decimals):
    return f"{value:.{decimals}f}"


def find_root_fixed_point():
    x = sp.Symbol("x")

    def get_functions_from_user():
        f_str = input("f(x) = : ")
        g_str = input("g(x) = : ")

        f_expr = sp.sympify(f_str)
        g_expr = sp.sympify(g_str)
        f = sp.lambdify(x, f_expr, modules=["math"])
        g = sp.lambdify(x, g_expr, modules=["math"])

        return f, f_expr, g

    f, f_expr, g = get_functions_from_user()

    x0, error = [float(y) for y in input("x0, error: ").split(",")]

    table = PrettyTable(["n", "x_n", "f(x_n)", "g(x_n)"])
    n = 0

    while True:
        n += 1
        x = g(x0)
        fx = f(x0)

        table.add_row(
            [n, fixed_decimal(x, 7), fixed_decimal(fx, 7), fixed_decimal(x0, 7)]
        )

        if abs(fx) < error:  # Check convergence based on f(x)
            print(table)
            print(f"Approximate root: {x}")
            break

        x0 = x


if __name__ == "__main__":
    find_root_fixed_point()
