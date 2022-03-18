# Author: MOG 2/1/22

import re


ary = [1,5,504,222,100,150]

def reverse(array):
    final_array = []
    for x in array:
        final_array.insert(0,x)
    print(final_array)
    
reverse(ary)