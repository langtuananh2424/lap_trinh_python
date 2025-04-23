import math

N = int(input("N = "))
F = 0
S = 0
for i in range(1, N+1):
    S += i
    F += math.sqrt(S)
print("F(%d) = {:.7f}".format(F)%N)
