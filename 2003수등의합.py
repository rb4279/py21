
n , m = map(int,input().split())
array = list(map(int, input().split()))


interval = 0
count = 0
end = 0

for start in range(0,n):
    while interval < m and end < n:
        interval += array[end]
        end += 1
    if interval == m :
        count += 1
    interval -= array[start]

print(count)
