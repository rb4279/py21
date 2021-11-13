import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
ans = []
# ans2 = []
# ans3 = []
interval_sum = 0 

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += arr[end]
        end += 1

    if interval_sum >= s:
        ans.append(end - start)
        # ans2.append((start,end))
    interval_sum -= arr[start]

if ans :
    print(min(ans))
else :
    print(0)