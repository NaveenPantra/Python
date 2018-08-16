def large_cont_sum(arr):
    maxi = 0
    start = 0
    end = 0
    for i in range(0, len(arr) - 1):
        sumE = arr[i]
        for j in range(i + 1, len(arr)):
            sumE += arr[j]
            if sumE > maxi:
                maxi, start, end = sumE, i, j

    return [maxi, start, end]


print(f"{large_cont_sum([1, 2, 3, -3, 7, 1, -3])}")


def large_cont_sum2(arr):
    maxS = curS = arr[0]
    for num in arr[1:]:
        curS = max(curS + num, num)
        maxS = max(maxS, curS)
    return maxS


print(f"{large_cont_sum2([1, 2, 3, -3, 7, 1, -3])}")
