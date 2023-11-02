import time
import ctypes
from numpy import ctypeslib as npct

a = 0
b = 2
rectangles = 900000000

LIB = "./calc_area_2.so"
lib = npct.load_library(LIB, ".")
calc_area_2 = lib.calc_area_2
calc_area_2.restype = ctypes.c_double
calc_area_2.argtypes = [ ctypes.c_double, ctypes.c_double, ctypes.c_int ]


start = time.time()

result = calc_area_2(a, b, rectangles)

end = time.time()


print("Result is " + str(result))
print("Elapsed time: " + str(end-start))