import heapq
import sys
input = sys.stdin.readline
inf = int(1e9) # 1000* 100000
v , e = map(int,input().split())
start_node = 1
graph = [[] for _ in range(v+1)]

# 입력
for i in range(e):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

second_node , third_node = map(int, input().split())

# 
def dijktra(start,dista):
    q = []
    heapq.heappush(q,(0,start))
    dista[start] = 0
    
    while q:
        dist , now = heapq.heappop(q)
        if dista[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < dista[i[0]]:
                dista[i[0]] = cost
                heapq.heappush(q, (cost , i[0]))


distance = [inf]*(v + 1)
distance2 = [inf]*(v + 1)
distance3 = [inf]*(v + 1)

dijktra(start_node,distance)
dijktra(second_node,distance2)
dijktra(third_node,distance3)

temp = distance[second_node] + distance2[third_node] + distance3[v]
temp2 = distance[third_node] + distance3[second_node] + distance2[v]
result = min(temp,temp2)
if result >= inf:
    print(-1)
else:
    print(result)