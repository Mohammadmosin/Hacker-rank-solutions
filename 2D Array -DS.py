#Hckerrank link: https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    l3=[]
    s1=0
    maxi=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i+2 <len(arr) and j+2 <len(arr):
                s1=sum(arr[i][j:j+3])+(arr[i + 1][j + 1])+sum(arr[i+2][j:j+3])
                if i==0 and j==0:
                    maxi=s1
                if maxi < s1:
                    maxi=s1
    return(maxi)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
