# -*-coding:utf8
#
"""
1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는?
"""

a=range(1, 101) # 1부터 100까지 있는 리스트 a를 작성
b=[] # 나중 계산을 위해 만든 빈 리스트
number2 = sum(a) # 리스트 a의 원소들 합을 구한다

print sum(a) # 계산이 맞는지 확인

while len(a) !=0: # 리스트 a의 원소가 다 사라질 때까지 반복
    number1 = a.pop(0) # while을 이용해 리스트 a의 원소들을 하나씩 빼서 제곱한다
    b.append(number1**2) # 제곱한 숫자들을 리스트 b로 넣는다
print sum(b) # 리스트 b의 원소들 합을 구한다.

print number2**2 # 앞에서 구한 1부터 100까지의 합에 제곱한다

print number2**2 - sum(b) # 합의 제곱에서 제곱의 합을 뺀다
