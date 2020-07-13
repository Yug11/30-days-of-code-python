#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().split(" ")))

# Write Your Code Herepass
numberOfSwaps = 0
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps+=1

print("Array is sorted in %s swaps."%numberOfSwaps)
print("First Element: %s"%a[0])
print("Last Element: %s"%a[-1])

