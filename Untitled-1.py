
'''

1부터 100 혹은 가장높은 수 만큼 반복
각각의 높이마다 높이보다 큰것을 찾아 깊이 우선 탐색

'''

import sys
sys.setrecursionlimit(100000)


def dfs(lst , h , w):
    if(lst[h][w] <= rainfall) or (check[h][w] == True):
        return False
    else :
        check[h][w] == True
        h_way_lst = [0,0,-1,1]
        w_way_lst = [1,-1,0,0]
        for i in range(4):
            h_way = h + h_way_lst[i]
            w_way = w + w_way_lst[i]
            if h_way< 0 or h_way>=N or w_way < 0 or w_way >= N or lst[h][w] <= rainfall or check[h][w] == True:
                    continue
            else :
                dfs(lst, h_way, w_way)
        return True
    
    


N = int(input())
lst = []
big_lst = []
for i in range(N):
    temp = list(map(int, input().split()))
    big_lst.append(max(temp))
    lst.append(temp)
big = max(big_lst)
max_count = 0

for rainfall in range(2,big+1):
    check =[ [False for x in range(N) ] for z in range(N) ]
    count = 0
    for i in range(N):
        for j in range(N):
            
            if dfs(lst,i,j) == True:
                count += 1
    if max_count < count :
        max_count = count

print(max_count)


    


