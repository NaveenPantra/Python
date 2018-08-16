
def coinChange(targetAmt, coins):
    minCoins = targetAmt

    if targetAmt in coins:
        return 1

    else:
        for coin in [smallCoin for smallCoin in coins if smallCoin <= targetAmt]:
            numCoins = 1 + coinChange(targetAmt - coin, coins)
            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins


print(f"{coinChange(10, [1, 5, 10])}")


def coinChangeMemo(targetAmt, coins, cache):
    minCoins = targetAmt

    if targetAmt in coins:
        cache[targetAmt] = 1
        return 1
    elif targetAmt in cache:
        return cache[targetAmt]
    else:
        for coin in [smallCoin for smallCoin in coins if smallCoin <= targetAmt]:
            numCoins = 1 + coinChangeMemo(targetAmt - coin, coins, cache)
            if numCoins < minCoins:
                cache[targetAmt] = minCoins = numCoins
    return minCoins


print(f"{coinChangeMemo(10, [1, 5, 10], {})}")
print(f"{coinChangeMemo(63, [1, 5, 10, 25], {})}")
