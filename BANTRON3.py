def find_last_person(N):
    last_person = 0
    for i in range(1, N + 1):
        last_person = (last_person + 3) % i
    return last_person + 1
N = int(input("So nguoi ngoi quanh ban: "))
last_person = find_last_person(N)
print("Nguoi o lai cuoi cung la nguoi thu", last_person)