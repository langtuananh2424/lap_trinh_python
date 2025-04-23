
import math

N = int(input("N = "))
F = 0
sum = 0
for i in range(1, N+1):
    F += i**2
    sum += N / F

print("F(%d) = {:.7f}".format(sum) % N)
