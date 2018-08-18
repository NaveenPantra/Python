

class Head(object):
    def __init__(self, node = None, value = 0):
        self.node = node
        self.value = 0

class Node(object):
    def __init__(self, nextNode = None, prevNode = None, value = 0):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.value = value

class BucketSort(object):
    def __init__(self, arr):
        self.arr = arr
        self.temp = [0.0] * len(arr)
        self.sort()

        
    def insertEle(self, ele):
        pos = int(round(ele))
        flag = 0
        
        for index in range(1, len(self.temp)):
            flag = 1
            if self.temp[index] > ele:
                self.temp.insert(index, ele)
                break
            
        if flag == 0:
            self.temp.append(ele)
            
        self.temp[pos][0] += 1

        
    def sort(self):
        maxi = max(self.arr)
        nums = [10, 100, 1000, 10000, 100000]
        
        for index in range(10):
            self.temp.append([0])
            
        for index in range(1, len(nums)):
            if maxi <= nums[index]:
                maxi = nums[index - 1]
                break
            
        for index in range(0, len(self.arr)):
            self.arr[index] /= maxi
        
        for num in self.arr:
            self.insertEle(num)
   
        
bSort = BucketSort([1, 2, 3, 4, 100, 889])

