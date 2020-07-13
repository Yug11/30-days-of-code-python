#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    try:
        tip = (meal_cost*tip_percent)/100
    except ZeroDivisionError:
        tip = 0
    try:
        tax = (meal_cost*tax_percent)/100
    except ZeroDivisionError:
        tax = 0
    fval = round(meal_cost+tip+tax)
    return fval

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
