# Time Complexity: O(n * log(n))
# n --> because buildMaxHeap() run n times
# log(n) --> maxHeapify() will run n - 1 times for buildMaxHeap()

# minHeap --> Descending Order
# maxHeap --> Ascending Order


class HeapSort(object):
    def __init__(self, arr):
        self.heapSize = len(arr) - 1
        self.arr = arr
        self.buildMaxHeap()
        # self.buildMinHeap()
        self.heapSort()

    def heapSort(self):
        for index in range(1, len(self.arr))[::-1]:
            # Important!! As heapSize is set to len(arr) and when the largest element is swapped to last then it
            # should not be disturbed
            self.heapSize -= 1
            self.arr[index], self.arr[0] = self.arr[0], self.arr[index]
            self.maxHeapify(0)
            # self.minHeapify(0)

    def buildMaxHeap(self):
        for index in range(len(self.arr) // 2)[::-1]:
            self.maxHeapify(index)

    def maxHeapify(self, index):
        leftIndex = (index << 1) + 1
        rightIndex = (index << 1) + 2
        largestIndex = index
        if leftIndex <= self.heapSize and self.arr[leftIndex] > self.arr[largestIndex]:
            largestIndex = leftIndex
        if rightIndex <= self.heapSize and self.arr[rightIndex] > self.arr[largestIndex]:
            largestIndex = rightIndex
        if largestIndex != index:
            self.arr[largestIndex], self.arr[index] = self.arr[index], self.arr[largestIndex]
            self.maxHeapify(largestIndex)

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


heap = HeapSort([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
print(f"{heap.getHeap()}")
