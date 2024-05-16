import sympy as sp
from prettytable import PrettyTable

x = sp.symbols("x1 x2")


def get_funcs():

    functions = []

    while True:
        input_str = input("Sistemani tenglamarini kirit ( tugatish uchun 'e' ni ): ")

        if input_str.lower() == "e":
            break

        functions.append(input_str.lower())

    return functions


def compute_partial_derivative(functions):
    variables = sp.symbols(f"x1:{len(functions)}")
    partial_derivatives = []

    for func_str in functions:
        func = sp.parse_expr(func_str)
        partials = [sp.diff(func, var) for var in variables]
        partial_derivatives.append(partials)
    return partial_derivatives


def main():
    functions = get_funcs()
    print(compute_partial_derivative(functions))


if __name__ == "__main__":
    main()
