def cachdoi(N, M):
    tien = [5000, 2000, 1000, 500, 200]
    doi = 0
    for i in range(N // tien[0] + 1):
        for j in range(N // tien[1] + 1):
            for k in range(N // tien[2] + 1):
                for l in range(N // tien[3] + 1):
                    for m in range(N // tien[4] + 1):
                        if i * tien[0] + j * tien[1] + k * tien[2] + l * tien[3] + m * tien[4] == N and i + j + k + l + m <= M:
                            doi += 1
    return doi

N = int(input("N = "))
M = int(input("M = "))
print("Co %d phuong an doi tien"%cachdoi(N, M))
