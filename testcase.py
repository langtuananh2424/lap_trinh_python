def banggia():
    data = {}
    while True:
        name = input("  Ten mat hang: ")
        if not name:
            break
        price = float(input("  Gia ban hang: "))
        data[name] = {"price": price}
    return data

def hangton():
    data1 = {}
    while True:
        name = input("  Ten mat hang: ")
        if not name:
            break
        quantity = int(input("  So luong hang ton: "))
        data1[name] = {"quantity": quantity}
def thongke(banggia):
    sorted_data = sorted(data.items(), key=lambda x: (-x[1]["price"] * x[1]["quantity"], x[0]))
    for name, info in sorted_data:
        print(f"{name}: {info['quantity']} * {info['price']} = {info['quantity'] * info['price']}")
        
def value(data, data1):
    value = {}
    for name in data:
        value[name] = data[name]['price'] * data1[name]['quantity']

print("NHAP BANG GIA:")
data = banggia()
print("NHAP HANG TON:")
data1 = hangton()
print("Thong ke hang ton:")
value = value(data, data1)
print(value)

