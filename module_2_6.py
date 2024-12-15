n = int(input('Первое число головоломки - '))
COD = []
for i in range(1, 20):
    for j in range(1, 20):
        if i >= j:
            continue
        else:
            if n % (i + j) == 0:
                COD.append([i, j])
print(*COD)