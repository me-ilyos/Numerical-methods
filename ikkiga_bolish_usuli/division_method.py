import math

error = 0.001 

def a_value(a):
    print(f"a: {a}")
    return pow(a, 3) - math.sin(a)

def b_value(b):
    print(f"b: {b}")
    return pow(b, 3) - math.sin(b)

while True:
    a, b = [float(y) for y in input("a, b: ").split(',') ]
    
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
