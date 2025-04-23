def tinh_tong_chu_so_trong_so(number):
# Chuyển số thành xâu
    str_number = str(number)
    
    # Khởi tạo biến tổng
    total = 0
    
    # Duyệt qua từng ký tự trong xâu số
    for ch in str_number:
        # Chuyển ký tự thành số nguyên và cộng vào tổng
        digit = int(ch)
        total += digit

    return total

# Gọi hàm và truyền số cần tính tổng các chữ số

n = int(input('N = '))

s=2**n

tong = tinh_tong_chu_so_trong_so(s)
print("Tong = {}".format(tong))
