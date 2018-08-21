class StringCount(object):

    def __init__(self, string):
        self.string = string
        self.s = set()
        self.count = 0

    def getCount(self):
        for i in range(len(self.string)):
            subStr = self.string[i:]
            # print(f"subStr = {subStr}")
            for j in range(len(subStr)):
                sub = subStr[:len(subStr) - j]
                # print(f"sub = {sub}")
                if self.s.__contains__(sub):
                    continue
                self.count += 1
                self.s.add(sub)

        return self.count, self.s


strCount = StringCount("abcdee")
count, s = strCount.getCount()
print(f"{sorted(s)}")
