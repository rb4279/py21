import sys
sys.setrecursionlimit(1000000)

def dfs(lst, x, y,n,check):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if lst[x][y] == check:
        lst[x][y] = 0
        x_direction = [0,1,-1,0]
        y_direction = [1,0,0,-1] 
        for i in range(4):
            dfs(lst,x+x_direction[i],y+y_direction[i],n,check)
        return True

n = int(input())
lst = []
for i in range(n):
  lst.append(list(input()))

lst2 = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(lst[i][j])
        if tmp[j] == 'R':
            tmp[j] = 'G'
    lst2.append(tmp)

group_count = 0
group_count2 = 0

for i in range(n):
    for j in range(n):
        check = lst[i][j]
        if check != 0:
            dfs(lst,i,j,n,check)
            group_count += 1

for i in range(n):
    for j in range(n):
        check = lst2[i][j]
        if check != 0:
            dfs(lst2,i,j,n,check)
            group_count2 += 1

print(group_count , group_count2 )