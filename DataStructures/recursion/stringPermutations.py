# This find the permutations of the string given by replacing the string in different positions
# This gives with repetitions


def permutation(s):
    """
    To find the permutations of the given string, with repetitions allowed.
    :param s: String.
    :return: list containing all permutations with repetitions allowed.
    """
    if len(s) == 1:
        return [s]
    if len(s) == 2:
        return [s, s[::-1]]
    else:
        result = []
        for excludeCharPos in range(0, len(s)):
            letter = s[excludeCharPos]
            temp = permutation(s[0:excludeCharPos] + s[excludeCharPos + 1:])
            for subStringPos in range(0, len(temp)):
                result.append(f"{letter + temp[subStringPos]}")

        return result


print(f"{permutation('abc')}")


def permutationString(s):
    result = []
    if len(s) == 1:
        result = [s]
    else:
        for pos, letter in enumerate(s):
            for permute in permutationString(s[:pos] + s[pos + 1:]):
                result += [letter + permute]

    return result


print(f"{permutationString('abc')}")
