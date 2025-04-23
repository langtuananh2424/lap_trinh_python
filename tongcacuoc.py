import math
n = int(input("N = "))
def sum_divisors(n):
    result = sum(i for i in range(1,n+1) if n % i == 0)
    return result
print(f"Tong cac uoc so cua {n} la {sum_divisors(n)}")
