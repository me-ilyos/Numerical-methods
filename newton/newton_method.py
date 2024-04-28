import sympy as sp

error = 0.001


def represent_function():
    x = sp.Symbol("x")
    expr = x**3 - sp.sin(x)
    print(expr)
    return expr


def function_at_point(a=None, b=None):
    print(f"Point a: {a}") if a else f"Poin b: {b}"

    x = sp.Symbol("x")
    expr = represent_function()
    return expr.subs(x, a if a else b)


def derr_function_at_point(point):
    x = sp.Symbol("x")
    expr = represent_function()
    print("A: ", expr)
    derr = sp.diff(expr, point)

    print(f"f'(x) = {derr}")

    return derr.subs(x, point)


def main():
    x0 = 0

    a, b = [float(y) for y in input("a, b: ").split(",")]

    c = a - function_at_point(a) * (
        (b - a) / (function_at_point(b) - function_at_point(a))
    )

    if function_at_point(a) * function_at_point(c) < 0:
        x0 = a
    else:
        x0 = b

    while True:
        x = x0 - function_at_point(x0) / derr_function_at_point(x0)

        if abs(x - x0) < error:
            return x
        else:
            x0 = x


if __name__ == "__main__":
    main()
