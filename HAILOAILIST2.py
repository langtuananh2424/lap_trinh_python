A = []
B = []
N = int(input("Nhap N: "))
for i in range(N):
    value = input(f"Nhap gia tri thu {i+1}: ")
    try:
        value = int(value)
        A.append(value)
    except ValueError:
        try:
            value = float(value)
            A.append(value)
        except ValueError:
            B.append(value)

if len(A) > 0:
    avg = sum(A) / len(A)
    print(f"TBC cua A = {avg}")

print(f"B = {B}")
