'''

시간초과 계속나다가
dfs bfs 해보다가 그냥 스택이나 큐대신 집합으로 해봤음
어차피 최단거리도 아니고 전부 탐색할거 같아서

'''

import sys



input = sys.stdin.readline
r , c = map(int,input().split())
lst = []
for i in range(r):
    lst.append(list(input()))

q = set()
# sta = []
q.add((0,0,lst[0][0]))
result = 0

while q:
    a,b,log = q.pop()
    if len(log) > result:
        result = len(log)
    r_way = [a,a,a+1,a-1]
    c_way = [b+1,b-1,b,b]
    for i in range(4):
        rp = r_way[i]
        cp = c_way[i]
        if 0<= rp < r and 0<= cp < c and (lst[rp][cp]) not in log:
            q.add((rp,cp,log+lst[rp][cp]))
            
        

print(result)