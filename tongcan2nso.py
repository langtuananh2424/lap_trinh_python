import math

n = int(input("N = "))


def sumsqrtn(n):
    sum = 0
    for i in range(1, n+1):
        sum += math.sqrt(sum + i)
    return sum


print("F(%s)" % str(n), "=", round(sumsqrtn(n), 7))
