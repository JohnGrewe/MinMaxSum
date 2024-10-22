#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def miniMaxSum(arr):
    # Write your code here
    max = 0
    min = 0
    total = 0

    for i in range(len(arr)):
        total += arr[i]
        if i == 0:
            max = arr[i]
            min = arr[i]
        else:
            if arr[i] > max:
                max = arr[i]
            if arr[i] < min:
                min = arr[i]
    print(f"{total-max} {total-min}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
