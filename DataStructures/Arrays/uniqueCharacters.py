from itertools import groupby


def uniqueCharacters(st):
    for i in range(0, len(st)):
        if st.count(st[i]) > 1:
            return [False, st[i]]
    return [True, st]


def uniqueCharacters2(st):
    return len(set(st)) == len(st)


print(uniqueCharacters("asderthd"))
print(uniqueCharacters2("asderthd"))