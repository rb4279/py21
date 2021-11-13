
# 1339번
# N개의 단어, 0~9중 하나의 숫자로 치환, N개의 수를 합하는 문제
#수 합의 최대?

#<입력>
# 단어 개수 N
# N개 줄에 간어 하나씩 주어짐

# <해결 방안>
# 각 알파벳에 자리수 부여
# 자리수 큰 순서로 정렬 후 
# 9부터 하나씩 할당

import sys
input = sys.stdin.readline
###이거 주석해야 됨 왜???

# 단어 갯수 지정
word_n = int(input())

# 단어들 리스트 만들기
word_lst = []
for _ in range(word_n) :
    word_lst.append(input().strip())

# 문자들 마다에 곱해야할 수 딕셔너리화 시키기
#  {'G': 100, 'C': 1010, 'F': 1, 'A': 10000, 'D': 100, 'E': 10, 'B': 1}
new_word_dict = {}

for a in word_lst :
    cnt = 0
    for i in a :

        if i not in new_word_dict :
            new_word_dict[i] = 10 ** (len(a) - cnt - 1) 
            # 단어 길이 - 앞서 검사한 알파벳 개수 -1
            # -1하는 이유: 1의 자리 숫자 제외

        elif i in new_word_dict :
            new_word_dict[i] += 10 ** (len(a) - cnt - 1)
            # 해당 알파벳이 이미 dict에 있을 경우에는
            # 이미 저장된 값에 추가로 또 더해주는 방식

        cnt += 1 # 앞서 검사한 알파벳의 개수

# 딕셔너리 Key값을 내림차순으로 솔팅하고 9부터 차례대로 곱해주기
ans_list = sorted(list(new_word_dict.values()), reverse = True)

sum = 0
for i in range(len(ans_list)) :
    sum += ans_list[i] * (9 - i)
ans = sum
print(ans)
