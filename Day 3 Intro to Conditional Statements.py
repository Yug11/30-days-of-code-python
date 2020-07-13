#!/bin/python3

import math
import os
import random
import re
import sys

def fun1(N):
        if N%2==1:
            return "Weird"
        elif 2<=N<=5:
            return "Not Weird" 
        elif 6<=N<=20:
            return "Weird"
        else:
            return "Not Weird"

if __name__ == '__main__':
    N = int(input())
    a = fun1(N)
    print(a)

