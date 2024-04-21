import threading
import os

def do_sum():
    print(1+1)

def set_interval(func, sec):
        def func_wrapper():
            set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        print("HMMM")
        return t
    
set_interval(do_sum, 1)