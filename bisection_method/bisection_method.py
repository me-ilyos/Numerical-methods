from prettytable import PrettyTable
import math
import sympy as sp


def find_root_bisection():
    while True:
        x = sp.Symbol('x')

        def get_func_from_user():
            while True:

                try:
                    func_str = input("Funksiyani x ga nisbatan kiriting: ")
                    f_str = sp.sympify(func_str)
                    f = sp.lambdify(x, func_str, modules=['math'])
                    return f, f_str
                except SyntaxError:
                    print("Funksiya kiritishda sintaktik xatolik. Iltimos qayta urinib ko'ring.")
                except NameError:
                    print("Funksiya ichida noma'lum nom yoki funksiya ishlatilgan. Qaytadan kiriting.")
                except TypeError:
                    print("Funksiya ichida qo'llab bo'lmaydigan amallar bor. Qaytadan kiriting.")

        fx, fx_str = get_func_from_user()

        a, b, error = [
            float(y)
            for y in input(
                "Quyidagilarni kiriting a, b, error (a va b yechimga ega bolishi kerak.): "
            ).split(",")
        ]

        if fx(a) * fx(b) >= 0:
            print("a va b yechimga ega emas. Boshqatdan kiriting.")
        else:
            break
    n = 0

    print(f"\n\n(a,b) = [{a}, {b}], error = {error}")

    print(f"{fx_str} uchun: ")

    table = PrettyTable(["n", "C", "F(C)"])

    while True:
        n += 1
        c = (a + b) / 2
        fc = fx(c)

        table.add_row([n, round(c, 6), round(fc, 6)])

        if fx(a) * fc < 0:
            b = c
        else:
            a = c

        if abs(fc) < error:
            print(table)

            print(
                f"Echimga error: {error} bolganda {n} ta qadamda erishdik\nx: {c} da f(x)={fc}"
            )
            break


if __name__ == "__main__":
    find_root_bisection()
