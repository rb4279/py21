'''
주어진 숫자들 중에서 작은 수 두개를 비교하는것이 그리디
비교한 후에 새로운 수를 다시 리스트에 집어 넣어서 작은 수 2개를 찾아야함
그래서 힙을 이용해서 우선순위큐를 사용

힙 만들고 
2개빼고 합하고 다시 넣고
2개빼고 합하고 다시 넣고
n-1 번 반복  
혹은 힙이 빌때까지 반복 하려면 1개만 남게될때 까지 고려해야함


'''
import heapq 

N = int(input())
queue = []
result = 0

for i in range(N): 
    heapq.heappush(queue,int(input()))

for i in range(N-1) :
    a,b = [heapq.heappop(queue) , heapq.heappop(queue)]
    heapq.heappush(queue,a+b)
    result += a+b

print(result)
