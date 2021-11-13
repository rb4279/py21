import math
import sys
input = sys.stdin.readline


num = int(input())

n = num
array = [True for i in range(n + 1)]
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
    while i * j <= n :
        array[i * j] = False
        j += 1

prime_array = []
for i in range(2,num+1):
    if array[i] == True:
        prime_array.append(i)

count = 0
interval_sum = 0
end = 0
length_prime = len(prime_array)
for start in range(length_prime):
    while interval_sum < num and end < length_prime:
        interval_sum += prime_array[end]
        end += 1
    if interval_sum == num:
        count += 1
    interval_sum -= prime_array[start]

print(count)
