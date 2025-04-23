n = int(input("Nhap N: "))
a = []
b = []
c = []

for i in range(1,n+1):
    x = input(f"Nhap gia tri thu {i}: ")
    try:
        x = int(x)
        a.append(x)
    except ValueError:
        try:
            x = float(x)
            b.append(x)
        except ValueError:
            c.append(x)

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

print("A =", a)
print("B =", b)
print("C =", c)