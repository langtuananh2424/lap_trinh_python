S = input("Nhap S: ")
for i in range(0, len(S)):
    if S[-3:] != "!!!":
        S += "!"
print("Chuoi S sau khi xu ly:", S)