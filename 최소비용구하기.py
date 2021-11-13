import heapq
import sys
input = sys.stdin.readline
inf = int(1e9) # 1000* 100000
v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]

# 입력
for i in range(e):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
start_node , last_node = map(int,input().split())


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

print(distance[last_node])