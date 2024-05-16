import sympy as sp
from prettytable import PrettyTable


def get_funcs():

    functions = []

    while True:
        input_str = input("Sistemani tenglamarini kirit ( tugatish uchun 'e' ni ): ")

        if input_str.lower() == "e":
            break

        functions.append([input_str.lower()])

    for i in range(len(functions)):
        gx = input("Tenglamani g(x) kirit: ")

        functions[i].append(gx.lower())

    return functions


def get_initial_values(num_equations):
    while True:
        try:
            input_str = input(f"{num_equations} ta belgilangan boshlangich qiymati: ")
            values_list = input_str.split(",")

            if len(values_list) != num_equations:
                raise ValueError("Kiritilgan boshlangich qiymatlar mos emas.")

            initial_values = [float(val.strip()) for val in values_list]
            return initial_values

        except ValueError:
            print("Invalid input. Please enter numerical values separated by commas.")


def symbolize_gx_functions(gx_functions, num_vars):
    x = sp.symbols(f"x1:{num_vars + 1}")
    symbolic_gx_functions = []

    for func_str in gx_functions:
        symbolic_gx_functions.append(sp.sympify(func_str, locals={"x": x}))

    return symbolic_gx_functions


def fixed_point_iteration(gx_functions, initial_values, tolerance, max_iterations):
    next_values = initial_values
    iteration_count = 0

    while iteration_count < max_iterations:
        old_values = next_values

        next_values = calculate_next_values(gx_functions, old_values)

        max_difference = max(
            abs(new - old) for new, old in zip(next_values, old_values)
        )
        if max_difference < tolerance:
            return next_values, iteration_count

        iteration_count += 1

    print("Failed to converge within the maximum iterations.")
    return None, iteration_count


def calculate_next_values(gx_functions, values):
    x = sp.symbols(f"x1:{len(values) + 1}")
    next_values = []
    for func in gx_functions:
        result = func.subs([(var, val) for var, val in zip(x, values)])
        next_values.append(result)
    return next_values


def main():
    functions = get_funcs()
    initial_values = get_initial_values(len(functions))

    x = sp.symbols(f"x1:{len(initial_values)+1}")

    gx_functions = [
        sp.sympify(equation[1].split("=")[1], locals={"x": initial_values})
        for equation in functions
    ]

    lambdified = [sp.lambdify(x, func) for func in gx_functions]

    i = 0

    table = PrettyTable(["Yechim nchi qadami", "X1", "X2"])

    while i < 100:
        old_values = initial_values.copy()
        new_values = []

        for func in lambdified:
            result = func(*old_values)
            new_values.append(result)

        diffs = [abs(abs(new) - abs(old)) for new, old in zip(new_values, old_values)]

        max_error = max(diffs)

        table.add_row([i] + [sp.Float(val) for val in new_values])

        if max_error < 0.0001:
            new_values = [sp.Float(val) for val in new_values]
            print(table)
            print(f"\nYechim {i}ta qadam da yechildi: {new_values}")
            break

        initial_values = new_values

        i += 1


if __name__ == "__main__":
    main()
