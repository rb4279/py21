
import math
import sys
input = sys.stdin.readline
n,k = map(int , input().split())
array = [True for i in range(n + 1)]

count = 0
fl = 0

for i in range(2, n + 1):
    if array[i] == True:
        j = 1
    while i * j <= n :
        if array[i*j] == True:
            array[i * j] = False
            count += 1
            # print(count , k, i , j)
            if count == k:
                print(i * j)
                fl = 1
                break
        j += 1

    if fl == 1:
        break

print('')


