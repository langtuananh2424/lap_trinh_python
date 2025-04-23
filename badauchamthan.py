def kiemtravathemdau(s):
    if s.endswith('!!!'):
        print(f"Chuoi sau khi bo sung dau cham than: '{s}'")
    elif s.endswith('!!'):
        snew = s + '!'
        print(f"Chuoi sau khi bo sung dau cham than: '{snew}'")
    elif s.endswith('!'):
        snew = s + '!!'
        print(f"Chuoi sau khi bo sung dau cham than: '{snew}'")
    else :
        snew = s + '!!!'
        print(f"Chuoi sau khi bo sung dau cham than: '{snew}'")

s = input('Nhap chuoi: ')
kiemtravathemdau(s)

