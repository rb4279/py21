'''
도로의 길이 , 도시의 기름가격

지나온 도시 리스트
다음 도시까지의 필요한 거리

해당하는 거리만큼 
지나쳐온 도시중에서 가장 싼 도시에서 기름을 더 산다

'''

numOfstation = int(input())
need_list = list(map(int, input().split()))
oil_list = list(map(int, input().split()))
total_cost = 0
min_oil = oil_list[0]

for i in range(numOfstation-1):
    need = need_list[i]
    if min_oil > oil_list[i]:   # min 함수로 처리하려니 시간 초과가 나서 감점 되는 듯 함
        min_oil = oil_list[i]
    total_cost +=  min_oil * need
    
print(int(total_cost))

