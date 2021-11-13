
import math
import sys
input = sys.stdin.readline
n = 1000000

array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
    while i * j <= n :
        array[i * j] = False
        j += 1



while (1):
    num = int(input())
    if num == 0:
        break
    for i in range(3,num//2+1):
        if (array[i] == True) and (array[num - i] == True):
            print(str(num)+' = '+str(i)+' + '+str(num-i))
            break



