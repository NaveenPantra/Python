def cSum(n):
    if n == 1:
        return 1
    else:
        return n + cSum(n - 1)


def dSum(n):
    if n % 10 == n:
        return n
    else:
        return n % 10 + dSum(n//10)


print(f"{cSum(4)}")
print(f"{dSum(4321)}")