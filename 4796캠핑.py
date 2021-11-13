'''
20일중에 8일동안에 5일만 사용가능하다면 
5o 3x 5o 3x 4o 이런식으로 초반에 가능한 뭉쳐있어야함  

v를 연속가능한 수 연속으로 불가능한 수 번갈아서 빼고
0보다 작아진 시점에서 마지막에 가능한수를 계산햇었다면 넘친만큼 뺴주고 (음수면 더하는식으로)
불가능한 수를 계산했다면 그냥 넘김 
'''
L , P , V = map(int,input().split())
count = 0
while L:
    count += 1
    result = 0
    x = P - L
    o = L
    flag = 0
    while V > 0:
        if flag == 0:
            V -= o
            flag = 1
            result += o
        else :
            V -= x
            flag = 0
    
    if V < 0  and flag == 1:  # o 을 계산한 이후라면 x를 기대하므로 flag가 1로 바뀌었을 것임
        result += V
    
    print('Case '+ str(count) +': '+str(result))


    L , P , V = map(int,input().split())
    