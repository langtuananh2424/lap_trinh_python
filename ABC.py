a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

lst = [a, b, c]
lst = list(set(lst))
lst.sort()
print(f"Xep tang dan:", end=' ')
for i in range(0, len(lst)):
    if (i == len(lst) - 1):
        print(lst[i])
    else:
        print(lst[i], end=' ')