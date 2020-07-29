import pandas as pd 
import math
import numpy as np

def fib(high, low, period):
    max_high = max(high[-(period):])
    min_low = min(low[-(period):])

    middle = (max_high + min_low)/2

    diff = max_high - min_low
    level0 = max_high
    level1 = min_low
    level236 = min_low + 0.236 * diff
    level382 = min_low + 0.382 * diff
    level618 = min_low + 0.618 * diff 
    level786 = min_low + 0.786 * diff 

    return level0, level236, level382, middle, level618, level786, level1

