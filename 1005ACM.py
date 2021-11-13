
import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    v,e = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    check = [0]*(v+1)

    indegree = [0] * (v + 1)
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    lastbuilding = int(input())

    def topology_sort():
        result = []
        q = deque()

        for i in range(1,v+1):
            if indegree[i] == 0:
                q.append(i)
                check[i] = cost[i]

        while q:
            now = q.popleft()
            # result.append(now)
            temp = 0
            for i in graph[now]:
                indegree[i] -= 1
                if check[i] == 0:
                    check[i] = cost[i] + check[now]
                else :
                    temp = cost[i] + check[now]
                    check[i] = max(check[i] , temp)
                
                if indegree[i] == 0:
                    q.append(i)
                    


        print(check[lastbuilding])

    topology_sort()
