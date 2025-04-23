def isEvenFibonacciNumber(n):
    a, b = 0, 1
    while b <= n:
        if b % 2 == 0:
            if b == n:
                return True
            else:
                a, b = b, a + b
        else:
            a, b = b, a + b
    return False

# Nhập số nguyên N từ bàn phím
N = int(input("N = "))

if isEvenFibonacciNumber(N):
    print("N la so fibonacci chan")
else:
    print("N khong phai la so fibonacci chan")
