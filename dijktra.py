
import heapq

INF = int(1e9)
node_num , edge_num = map(int , input().split())
start_nod = int(input())

graph = [[] for _ in range(node_num+1)]
distance = [INF] * (N + 1)

for i in range(M):
    x,y,edge_cost = map(int ,input().split())
    graph[x].append((y,edge_cost))


def dijktra(start_node):
    q = []
    heapq.heappush(q,(0,start_node))
    distance[start_node] = 0
    
    while q:
        dist , now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost , i[0]))


for i in range(1, N+1):
    if distance[i] != INF:
        print(i, distance[i])

    else:
        print("INF")