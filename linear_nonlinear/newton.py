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
        functions.append(input_str.lower())
    return functions


def compute_partial_derivatives(functions):
    """Computes symbolic partial derivatives."""
    variables = sp.symbols(f"x1:{len(functions) + 1}")
    partial_derivatives = []
    for func_str in functions:
        func = sp.parse_expr(func_str)
        partials = [sp.diff(func, var) for var in variables]
        partial_derivatives.append(partials)
    return partial_derivatives


def evaluate_partial_derivatives(partial_derivatives, initial_values, variables):
    """Evaluates partial derivatives at initial values."""
    substitutions = dict(zip(variables, initial_values))
    evaluated_partials = []
    for partials in partial_derivatives:
        evaluated_row = [
            float(partial.subs(substitutions).evalf()) for partial in partials
        ]  # Use evalf() and float()
        evaluated_partials.append(evaluated_row)
    return np.array(evaluated_partials, dtype=float)


def calculate_function_values(functions, initial_values):
    """Calculates function values at initial values."""
    variables = sp.symbols(f"x1:{len(functions) + 1}")
    substitutions = dict(zip(variables, initial_values))
    function_values = []
    for func_str in functions:
        func = sp.parse_expr(func_str)
        value = float(func.subs(substitutions).evalf())  # Use evalf() and float()
        function_values.append(value)
    return function_values  # Return as a list of floats


def invert_jacobian(evaluated_partials):
    """Inverts the Jacobian matrix."""
    try:
        inverse_jacobian = np.linalg.inv(evaluated_partials)
        return inverse_jacobian
    except np.linalg.LinAlgError:
        print("Warning: Jacobian is singular (not invertible) at this point.")
        return None


def multiply_inverse_jacobian_by_f(inverse_jacobian, function_values):
    """Multiplies the inverse Jacobian matrix by the function values."""
    if inverse_jacobian is not None:
        delta_x = -np.dot(inverse_jacobian, function_values)
        return delta_x
    else:
        return None


def main():
    functions = get_funcs()
    initial_values = np.array(
        [float(y) for y in input("Enter initial values (comma-separated): ").split(",")]
    )
    variables = sp.symbols(f"x1:{len(functions) + 1}")

    partial_derivatives = compute_partial_derivatives(functions)

    tolerance = 1e-6
    max_iterations = 100
    table = PrettyTable()
    table.field_names = [f"x{i+1}" for i in range(len(initial_values))] + ["||f(x)||"]

    current_values = initial_values
    for iteration in range(max_iterations):
        function_values = calculate_function_values(functions, current_values)

        # Check for convergence early
        if all(
            abs(f) < tolerance for f in function_values
        ):  # Check absolute values and use 'all' for lists
            print(table)
            print(f"Newton's method converged after {iteration} iterations.")
            break

        # Ensure function_values is always an array, even with a single value
        function_values = np.array(function_values)  # Convert list to array

        evaluated_partials = evaluate_partial_derivatives(
            partial_derivatives, current_values, variables
        )
        inverse_jacobian = invert_jacobian(evaluated_partials)
        if inverse_jacobian is not None:
            delta_x = multiply_inverse_jacobian_by_f(inverse_jacobian, function_values)

            if delta_x is not None:
                current_values = current_values - delta_x

                # Add row to the table (rounding and handling scalar function values)
                rounded_values = [round(x, 4) for x in current_values]
                rounded_norm = round(
                    float(np.linalg.norm(function_values)), 4
                )  # Convert to float and round
                table.add_row(
                    rounded_values + [rounded_norm]
                )  # Directly add rounded_norm
            else:
                print("Newton's method update failed due to a singular Jacobian.")
                break
        else:
            print("Jacobian inversion failed.")
            break


if __name__ == "__main__":
    main()
