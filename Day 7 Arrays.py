#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
ans = ""
for i in range(len(arr)-1 , -1, -1):
    ans += str(arr[i]) + " "
print(ans)
