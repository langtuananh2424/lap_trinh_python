
import math


n = int(input("N = "))
s = 0
s1 = 0
for i in range(1, n+1):
    s1 += i
    s += s1**(1/i)

print("F(%d) = {:.7f}".format(s) % n)
