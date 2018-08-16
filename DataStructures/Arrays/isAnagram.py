def is_anagram(s1, s2):
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')
    print(f"{s1}, {s2}")
    if len(s1) == len(s2):
        for i in range(0, len(s1)):
            print(f"{s1.count(s1[i])} {s2.count(s1[i])}")
            if not s1.count(s1[i]) == s2.count(s1[i]):
                return False
        return True

    return False


def is_anagram2(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    print(f"{sorted(s1)}, {sorted(s2)}")
    return sorted(s1) == sorted(s2)


print(f"{is_anagram2(' dsf   krds HIAasdf', 'kdha sd   ir  ASDFsf')}")
