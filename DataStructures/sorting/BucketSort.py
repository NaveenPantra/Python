# If the Implementation with Linked Lists

# class Head(object):
#     def __init__(self, node = None, value = 0):
#         self.node = node
#         self.value = 0
#
#
# class Node(object):
#     def __init__(self, nextNode = None, prevNode = None, value = 0):
#         self.nextNode = nextNode
#         self.prevNode = prevNode
#         self.value = value


class BucketSort(object):
    def __init__(self, arr):
        self.arr = arr
        self.temp = []
        self.sort()

    def insertEle(self, ele):
        pos = int(round(ele))
        flag = 0
        for index in range(1, len(self.temp[pos])):
            flag = 1
            if ele < self.temp[pos][index]:
                self.temp[pos].insert(index, ele)
                break
            elif index == len(self.temp[pos]) - 1:
                self.temp[pos].append(ele)
        if flag == 0:
            self.temp[pos].append(ele)
        self.temp[pos][0] += 1

    def sort(self):
        maxi = max(self.arr)
        nums = [10, 100, 1000, 10000, 100000, 1000000]
        for index in range(10):
            self.temp.append([0])
        for index in range(1, len(nums)):
            if maxi <= nums[index] and maxi :
                maxi = nums[index]
                break
        for index in range(0, len(self.arr)):
            self.arr[index] *= 1.0
            self.arr[index] /= maxi
        for num in self.arr:
            self.insertEle(num)
        for li in self.temp:
            if li[0] > 0:
                for ele in li[1:]:
                    print(f"{int(ele * maxi)}, ", end='')
        print(f"\b\b", end='')


bSort = BucketSort([1, 200, 3000, 40000, 100, 1000, 999, 234, 134, 908, 456, 0])
