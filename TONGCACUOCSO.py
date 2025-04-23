import math

N = int(input("N = "))
sum = 0

for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        sum += i
        if N // i != i:
            sum += N//i
        
print(f"Tong cac uoc so cua {N} la {sum}")
