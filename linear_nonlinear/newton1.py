import re

import numpy as np
import sympy as sp
from prettytable import PrettyTable


def get_funcs():
    """Gets functions from user input."""
    functions = []
    while True:
        input_str = input("Enter the equation of the system (enter 'e' to finish): ")
        if input_str.lower() == "e":
            break
        functions.append(input_str)
    return functions


def newton_method(equations, x0_list, tol=1e-6, max_iter=100):
    """Solves a system of nonlinear equations using Newton's method."""
    variables = sorted(set(re.findall(r"[a-zA-Z]\w*", "".join(equations))))
    symbols = sp.symbols(variables)
    sp_equations = [sp.parse_expr(eq) for eq in equations]

    f = sp.Matrix(sp_equations)
    J = f.jacobian(symbols)

    x = np.array(x0_list, dtype=float)

    table = PrettyTable()
    table.field_names = ["k"] + variables

    for k in range(max_iter):
        subs_dict = {sym: val for sym, val in zip(symbols, x)}
        f_val = np.array(f.subs(subs_dict)).astype(float)
        J_val = np.array(J.subs(subs_dict)).astype(float)

        delta = np.linalg.solve(J_val, -f_val)
        delta = delta.reshape(x.shape)
        x += delta

        table.add_row([k] + [f"{val:.8f}" for val in x])

        if np.linalg.norm(delta) < tol:
            break

    print(table)


if __name__ == "__main__":
    equations = get_funcs()
    if not equations:
        print("No equations entered.")
    else:
        x0_str = input("Enter initial guesses (space-separated): ")
        x0_list = [float(x) for x in x0_str.split()]

        newton_method(equations, x0_list)
