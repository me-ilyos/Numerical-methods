error = 0.001 

def a_value(a):
    print(f"a: {a}")
    return ((4 - a) + ((a-1)/(a+1) ** 1/3))

def b_value(b):
    print(f"b: {b}")
    return ((4 - b) + ((b-1)/(b+1) ** 1/3))

while True:
    a, b = [int(y) for y in input("a, b: ").split(',') ]
    
    if a_value(a) * b_value(b) < 0:
        while True:
            c = (a + b) / 2
            if a_value(a) * b_value(c) < 0:
                b = c
            else:
                a = c

            if abs(a_value(a) - b_value(b)) < 0.001:
                print(f"Tenglamani taqribiy echimi: {c}\nFarqi: {abs(a_value(a) - b_value(b))}")
                break
