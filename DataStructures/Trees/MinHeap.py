class MinHeap(object):
    def __init__(self, arr):
        self.heapSize = len(arr) - 1
        self.arr = arr
        self.buildMinHeap()

    def buildMinHeap(self):
        for index in range(len(self.arr) // 2)[:: -1]:
            self.minHeapify(index)

    def minHeapify(self, index):
        leftIndex = (index << 1) + 1
        rightIndex = (index << 1) + 2
        smallestIndex = index
        if leftIndex <= self.heapSize and self.arr[leftIndex] < self.arr[smallestIndex]:
            smallestIndex = leftIndex
        if rightIndex <= self.heapSize and self.arr[rightIndex] < self.arr[smallestIndex]:
            smallestIndex = rightIndex
        if smallestIndex != index:
            self.arr[smallestIndex], self.arr[index] = self.arr[index], self.arr[smallestIndex]
            self.minHeapify(smallestIndex)

    def getHeap(self):
        return self.arr


heap = MinHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
print(f"{heap.getHeap()}")
