# run_c_so_from_python.py

from ctypes import *

if __name__ == '__main__':    
    my_functions = CDLL("./15.so")
    my_functions.func.restype = c_double
    print(my_functions.func(10))