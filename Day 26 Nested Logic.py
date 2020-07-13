# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

Da, Ma, Ya = list(map(int, input().strip().split(' ')))
Db, Mb, Yb = list(map(int, input().strip().split(' ')))

if Ya == Yb:
    if Ma == Mb:
        if Da == Db:
            print("0")
        elif Da > Db:
            fine = 15*(Da-Db)
            print(fine)
        else:
            print("0")

    elif Ma > Mb:
        fine = 500*(Ma-Mb)
        print(fine)
    else:
        print("0")
elif Ya > Yb:
    print("10000")
else:
    print("0")
