
'''

1부터 100 혹은 가장높은 수 만큼 반복
각각의 높이마다 높이보다 큰것을 찾아 깊이 우선 탐색

스택 오버플로우여서 재귀 함수 없애버림

'''

from collections import deque

def bfs(h , w, check):
    if(check[h][w] <= rainfall) or (check[h][w] == 0):
        return False
    else :
        # sta = []
        q = deque()
        # sta.append((h,w))
        q.append((h,w))
        check[h][w] = 0

        while q:
            hp,wp = q.pop()

            h_way_lst = [0,0,-1,1]
            w_way_lst = [1,-1,0,0]
            for i in range(4):
                h_way = hp + h_way_lst[i]
                w_way = wp + w_way_lst[i]
                if h_way< 0 or h_way>=N or w_way < 0 or w_way >= N or (check[h_way][w_way] <= rainfall) or (check[h_way][w_way] == 0):
                        continue
                else :
                    q.append((h_way, w_way))
                    check[h_way][w_way] = 0
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
count_lst = []

for rainfall in range(big): 
    check =[]
    for i in range(N):
        check.append([])
        for j in range(N):
            check[i].append(lst[i][j])
    count = 0
    
    for i in range(N):
        for j in range(N):
            if bfs(i,j,check) == True:
                count += 1
    # count_lst.append(count)
    if max_count < count:
        max_count = count
print(max_count)

    


