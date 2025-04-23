n = int(input('Nhap N duong: '))

f=0
giaithua=1

for i in range (1,n+1):
    giaithua *= i
    f += giaithua
    
print(f'F({n}) = {f}') 