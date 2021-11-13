import heapq
import sys
input = sys.stdin.readline
inf = 10001
m, n = map(int, input().split())
# 세로방향을 x,n 으로 표현함
graph = [[1]*(m+1)]

# 입력
for i in range(n):
    graph.append([1]+list(map(int,input().rstrip())))





# 
queue = []
distance = [[inf]*(m + 1) for _ in range(n+1)]
distance[1][1] = 0

heapq.heappush(queue, (0,1,1))

while queue:
    now_cost , nowx, nowy = heapq.heappop(queue)
    if distance[nowx][nowy] < now_cost:
        continue

    xp = [0, 0, 1, -1]
    yp = [1, -1, 0, 0]
    for i in range(4):
        x =nowx + xp[i]
        y =nowy + yp[i]
        if x<1 or x>n or y<1 or y>m:
            continue
        cost = now_cost + graph[x][y]
        if cost < distance[x][y]:
            distance[x][y] = cost
            heapq.heappush(queue, (cost, x,y))

temp = distance[n][m]
if temp == inf:
    print("INF") ## 항상 뜷려있으므로 나올일 없음
else:
    print(temp)