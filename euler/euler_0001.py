# -*-coding:utf8
# problem 1
"""
10보다 작은 자연수 중 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.
1000보다 작은 자연수 중 3또는 5의 배수를 모두 더하면?
"""

x = range(1, 1000)
y = []

for number in x:
    if number % 3 == 0 or number % 5 == 0:
        y.append(number)

print sum(y)