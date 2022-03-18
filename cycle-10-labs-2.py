# Author: MOG 2/1/22

from turtle import done, end_fill
from typing import final


nums = [1,5,504,222,100,150]

def fun(nums):
    final_nums = []
    for x in nums:
        if x <= 150 and x % 5 == 0:
            final_nums.append(x)
        elif x > 500:
            break
    print(final_nums)
    
fun(nums)