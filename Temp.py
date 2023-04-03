a = [[0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

def find_one(x):
    count = 0
    for i in range(len(x)):
        for g in range(len(x[i])):
            if x[i][g] == 1:
                count += 1
                check_near(a, i, g)
    return count

def check_near(x, q, w):
    if w < (len(a[q]) - 1) and x[q][w + 1] == 1:
        x[q][w + 1] = 0
        check_near(x, q, w + 1)
    elif q < (len(a) - 1) and x[q + 1][w] == 1:
        x[q + 1][w] = 0
        check_near(x, q + 1, w)
    elif w > 1 and x[q][w - 1] == 1:
        x[q][w - 1] = 0
        check_near(x, q, w - 1)
    elif q > 0 and x[q - 1][w] == 1:
        x[q - 1][w] = 0
        check_near(x, q - 1, w)
    else:
        return 1

print(find_one(a))


