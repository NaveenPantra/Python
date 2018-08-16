from collections import defaultdict


def missing_number(sarr, rarr):
    missing = []
    for i in sarr:
        if sarr.count(i) != rarr.count(i):
            missing.append(i)
    return missing


print("", format(missing_number([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 6, 7, 4])))


def missing_number2(sarr, rarr):
    sarr.sort()
    rarr.sort()
    for num1, num2 in zip(sarr, rarr):
        if num1 != num2:
            return num1


print("", format(missing_number2([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 6, 7, 4])))


def missing_number3(sarr, rarr):
    di = defaultdict(int)
    for num in rarr:
        di[num] += 1

    for num in sarr:
        if di[num] == 0:
            return num


print("", format(missing_number3([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 6, 7, 4])))


def missing_number4(sarr, rarr):
    result = 0
    for num in sarr + rarr:
        result ^= num
    return result


print("", format(missing_number4([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 6, 7, 4])))