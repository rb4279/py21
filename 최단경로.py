import heapq
import sys
input = sys.stdin.readline
inf = 3000001
v, e = map(int, input().split())
start_node = int(input())
graph = [[] for _ in range(v+1)]

# 입력
for i in range(e):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))


# 
queue = []
distance = [inf]*(v + 1)
distance[start_node] = 0
heapq.heappush(queue, (0,start_node))

while queue:
    now_cost , now = heapq.heappop(queue)
    if distance[now] < now_cost:
        continue
    for i in graph[now]:
        cost = now_cost + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0]))

for i in range(1,v+1):
    temp = distance[i]
    if temp == inf:
        print("INF")
    else:
        print(distance[i])