"""
A simple decorator which will pause a function for a random no. of seconds.
The range will be provided by when calling the fubction. This decorator can be 
applied to any function.


steps:
   1. First we will import the required modules
"""

from functools import wraps
import random
import time


def pause_func(min, max):
    def decor(func):
        @wraps(func)
        def inner(*args, **kwargs):
            
            start_time = time.time()
            time.sleep(random.randint(min, max))
            end_time = time.time()
            print("This function was paused for {}".format(end_time-start_time))
            return func(*args, **kwargs)
        return inner
    return decor
    

@pause_func(1,10)
def multiply(x,y):
    print("x *y = ",x*y)
    
    
@pause_func(1,5)    
def loop():
    for i in range(10):
        pass
        
        
        
multiply(1,2)
loop()