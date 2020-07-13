#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    ls = []
    ls = ""
    while n!=0:
        a = n%2
        n = int(n/2)
        ls+=str(a)
        
    lsr = ls[::-1]
    print(max(map(len,lsr.split('0'))))

