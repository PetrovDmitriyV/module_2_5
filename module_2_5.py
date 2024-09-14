def get_matrix(n, m, value):
    matrix = []
    a = []
    for i in range(n):
        if i >= 0:
            a = []
            matrix.append(a)
        else:
            break
        for j in range(m):
            if j >= 0:
                b = [value]
                a = [b * m]
                break
            else:
                break
    matrix = a * n
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)