a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

def check(a,b,c):
    if a+b <= c or a+c <= b or b+c <= a:
        print("Khong phai tam giac")
    else:
        print("Dung la tam giac")

check(a,b,c)