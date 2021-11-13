import heapq
import sys
input = sys.stdin.readline
inf = int(1e9) # 1000* 100000
v , e ,start_node= map(int,input().split())
graph = [[] for _ in range(v+1)]
graph2 = [[] for _ in range(v+1)]

# 입력
for i in range(e):
    a,b,cost = map(int,input().split())
    graph2[a].append((b,cost))
    graph[b].append((a,cost))


# 
queue = []
queue2 = []
distance = [inf]*(v + 1)
distance2 = [inf]*(v + 1)
distance[start_node] = 0
distance2[start_node] = 0
heapq.heappush(queue, (0,start_node))
heapq.heappush(queue2, (0,start_node))
while queue:
    now_cost , now = heapq.heappop(queue)
    if distance[now] < now_cost:
        continue
    for i in graph[now]:
        cost = now_cost + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0]))
while queue2:
    now_cost , now = heapq.heappop(queue2)
    if distance2[now] < now_cost:
        continue
    for i in graph2[now]:
        cost = now_cost + i[1]
        if cost < distance2[i[0]]:
            distance2[i[0]] = cost
            heapq.heappush(queue2, (cost, i[0]))

result = 0
for i in range(1,v+1):
    temp = distance[i] + distance2[i]
    if temp < inf :
        result = max(result,temp)
print(result)