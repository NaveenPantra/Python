from itertools import groupby


def stringCompression(st):
    """

    :param st:string
    :return cs:string
    """
    li = [[k, tuple(g)] for k, g in groupby(st, key=lambda k: k)]
    cs = ""
    for i in range(0, len(li)):
        cs += f"{li[i][0]}{len(li[i][1])}"
        # print(f"{li[i][0]}{len(li[i][1])}")
    # print(f"{cs}")
    return cs


stringCompression("aaabbaaaccccdd")
print(help(stringCompression))