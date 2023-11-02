import math
import time

def f(x):
    return (math.sin(x)**3) + (math.cos(x)**3)

def calc_area(a, b, rectangles, f):
    
    start = time.time()

    delta_x = (b - a)/rectangles

    acc_area = 0

    k = delta_x

    while (k <= b):
        acc_area += delta_x*f(k)
        k += delta_x
        
    
    print("The area is " + str(acc_area) + " units")

    end = time.time()

    print("Elapsed time: " + str(end-start))


# CALL

calc_area(0,2, 900000000, f)


