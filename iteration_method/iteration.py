import sympy as sp

x = sp.Symbol("x")


x0, error = [float(y) for y in input("x0, error: ").split(",")]


def function_at(x0):
    x = sp.Symbol("x")
    expr = sp.cbrt((4 * x + 800))

    return expr.subs(x, x0)


def function_at1(x0):
    x = sp.Symbol("x")
    expr = 0.1 * (x**3) - 0.4 * x - 80

    return expr.subs(x, x0)


while True:
    x = function_at(x0)

    if abs(x - x0) < error:
        print(f"{x} | {function_at1(x): 6.8f}")
        break
    else:
        # print(x0, function_at1(x), sep=" ||| ")
        print(f"{x0} | {function_at1(x): 6.5f}")
        x0 = x
