# -*-coding:utf8
"""
피보나치 수열의 각 항은 바로 앞의 항 두개를 더한것이 된다
짝수이면서 4백만 이하인 모든 항을 더하면?
4백만 이상인 최초의 항은?
"""

def fibonacci(n):
    if 1 == n:
        return 1
    if 2 == n:
        return 2
    if 0 >= n:
        return 0
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def main():
    for i in range(1, 10 + 1):
        print"Fibonacci(%d) = %d" % (i, fibonacci(i))

    i = 11
    while True:
        f = fibonacci(i)
        if f > 4000000:
            print "Fibonacci(%d) = %d" % (i, f)
            exit(0)
        i += 1

if '__main__' == __name__:
    main()