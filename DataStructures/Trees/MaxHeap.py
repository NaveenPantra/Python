# 2i = (i << 1), 2i + 1 = (i << 1) + 1, 2i + 2 = (i << 1) + 2
# i / 2  =  i >> 1


class MaxHeap(object):

    def __init__(self, arr):
        self.heapSize = len(arr) - 1
        self.arr = arr
        self.buildMaxHeap()

    def buildMaxHeap(self):
        for index in list(range(len(self.arr)//2))[::-1]:
            self.maxHepify(index)

    def maxHepify(self, index):
        leftIndex = (index << 1) + 1
        rightIndex = (index << 1) + 2
        largestIndex = index
        if leftIndex <= self.heapSize and self.arr[leftIndex] > self.arr[largestIndex]:
            largestIndex = leftIndex
        if rightIndex <= self.heapSize and self.arr[rightIndex] > self.arr[largestIndex]:
            largestIndex = rightIndex
        if largestIndex != index:
            self.arr[largestIndex], self.arr[index] = self.arr[index], self.arr[largestIndex]
            self.maxHepify(largestIndex)

    def getHeap(self):
        return self.arr


heap = MaxHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
print(f"{heap.getHeap()}")

