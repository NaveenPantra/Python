def str_rev(s):
    if len(s) == 0:
        return s
    else:
        return s[len(s) - (len(s) + 1)] + str_rev(s[:len(s) - 1])


print(f"{str_rev('Naveen Pantra')}")


def str_rev2(s):
    if len(s) == 0:
        return s
    else:
        return str_rev2(s[1:]) + s[0]

print(f"{str_rev2('Naveen Pantra')}")