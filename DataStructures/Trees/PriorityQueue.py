class PQueues(object):
    def __init__(self, arr):
        self.heapSize = len(arr) - 1
        self.arr = arr
        self.buildMaxHeap()

    def buildMaxHeap(self):
        self.heapSize = len(self.arr) - 1
        for elementPos in list(range(len(self.arr) // 2))[::-1]:
            self.maxHepify(elementPos)

    def maxHepify(self, index):
        leftIndex = (index << 1) + 1
        rightIndex = (index << 1) + 2
        largestIndex = index
        if leftIndex <= self.heapSize and self.arr[leftIndex] > self.arr[index]:
            largestIndex = leftIndex
        if rightIndex <= self.heapSize and self.arr[rightIndex] > self.arr[largestIndex]:
            largestIndex = rightIndex
        if largestIndex != index:
            self.arr[largestIndex], self.arr[index] = self.arr[index], self.arr[largestIndex]
            self.maxHepify(largestIndex)

    def maximum(self):
        return self.arr[0]

    def extractMaximum(self):
        if self.heapSize <= 0:
            raise BufferError("Heap Underflow")
        maxi = self.arr[0]
        self.arr[0] = self.arr[self.heapSize]
        self.heapSize -= 1
        self.arr.pop()
        self.maxHepify(0)
        return maxi

    def increaseKey(self, index, key):
        if key < self.arr[index]:
            raise ValueError("Key cannot be less the previous key")
        self.arr[index] = key
        parentIndex = (index >> 1)
        while index > 0 and self.arr[parentIndex] < self.arr[index]:
            self.arr[parentIndex], self.arr[index] = self.arr[index], self.arr[parentIndex]
            index = parentIndex
            parentIndex >>= 1

    def insertKey(self, key):
        self.heapSize += 1
        self.arr.append(key)
        self.increaseKey(self.heapSize, key)

    def getHeap(self):
        return self.arr


heap = PQueues([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
print(f"Max-Heap: {heap.getHeap()}")
print(f"Maximum Element: {heap.maximum()}")
print(f"Extract-Max: {heap.extractMaximum()}")
heap.increaseKey(3, 15)
heap.insertKey(16)
heap.insertKey(30)
heap.insertKey(40)
print(f"Max-Heap: {heap.getHeap()}")
