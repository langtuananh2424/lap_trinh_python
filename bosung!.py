
S = input("Nhap chuoi: ")
for i in range(0, len(S)):
    if S[-3:] != "!!!":
        S += "!"
print(f"Chuoi sau khi bo sung dau cham than: '{S}'")