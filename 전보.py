import heapq

INF = int(1e9)

N , M , C = map(int, input().split())
city = [[] for _ in range(N+1)]
distance = [INF] * (N + 1)
for i in range(M):
    x,y,z = map(int ,input().split())
    city[x].append((y,z))


##
q = []
distance[0] = 0
heapq.heappush(q, (0,C))
while q:
    dist , now = heapq.heappop(q)

    if distance[now] < dist: 
        continue
    for i in city[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost , i[0]))

temp  = 0
tempi = 0

for i in range(1 , N+ 1):
    if (temp < distance[i]) and (distance[i] != INF):
        temp = distance[i]
        tempi = i
print(tempi, temp)