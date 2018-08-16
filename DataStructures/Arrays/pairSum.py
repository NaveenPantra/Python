from itertools import combinations


def pair_sum(arr, s):
    count = 0
    for i in combinations(arr, 2):
        if sum(i) == s:
            print(f"{i}")
            count += 1
    return count


# print(f"{pair_sum([1, 3, 2, 2], 4)}")


def pair_sum2(arr, s):
    count = 0
    for f in arr[:len(arr) - 1]:
        for l in arr[f:]:
            if (f + l) == s:
                print(f"{f}, {l}")
                count += 1
    return count


# print(f"{pair_sum2([1, 2, 3, 4, 5, 6, 7], 6)}")


def pair_sum3(arr, s):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = s - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target, num), max(target, num)))

    print("\n".join(map(str, output)))


pair_sum3([1, 2, 3, 4, 5, 6, 7], 6)