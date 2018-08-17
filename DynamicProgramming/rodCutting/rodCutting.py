def rodCutting(n, price):
    if n is 0: return 0
    maxi = -1
    for i in range(0, n):
        temp = price[n - i - 1] + rodCutting(i, price)
        maxi = max(temp, maxi)
    return maxi


print(rodCutting(5, [1, 5, 8, 9, 10]))