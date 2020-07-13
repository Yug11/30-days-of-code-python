# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

for i in range(0, N):

    string = input()
    print(string[::2],string[1::2])
