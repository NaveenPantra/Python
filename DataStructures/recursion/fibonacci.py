
def fiboR(n):
    if n <= 1:
        return n
    else:
        return fiboR(n - 1) + fiboR(n - 2)


print(f"{fiboR(10)}")


record = {0: 0, 1: 1}


def fiboM(n):
    if n in record:
        return record[n]
    else:
        record[n] = fiboM(n - 1) + fiboM(n - 2)
    return record[n]


print(f"{fiboM(10)}")


def fiboD(n):
    a, b = -1, +1
    i, c = 0, 0
    while i <= n:
        c = a + b
        # print(f"{c}  ")
        a, b = b, c
        i += 1
    return c

print(f"{fiboD(10)}")