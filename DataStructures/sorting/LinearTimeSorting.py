class CountingSort(object):
    def __init__(self, arr):
        self.arr = arr
        self.sortedArr = [0] * len(arr)
        self.countArr = [0] * (max(arr) + 1)
        self.countingSort()

    def countingSort(self):
        # Looping to increase the count of the element occurrence in the given array.
        for element in self.arr:
            self.countArr[element] += 1

        # This makeup the count of the each element and at last the number at each index represent,
        # the final index the element should occur,
        # By following the above method the STABLE property can be achieved.
        for index in range(1, len(self.countArr)):
            self.countArr[index] += self.countArr[index - 1]

        # The elements are inserted in to the sortedArr,
        # -1 in here because this the index start form '0' and end at 'n - 1' but nor at 'n',
        # When the element is inserted into the sortedArr then the count of the element in countArr will be decreased.
        for index in range(len(self.arr) - 1, -1, -1):
            self.sortedArr[self.countArr[self.arr[index]] - 1] = self.arr[index]
            self.countArr[self.arr[index]] -= 1

    def sort(self):
        return self.sortedArr


CSort = CountingSort([2, 5, 3, 0, 2, 3, 0, 3, 10, 300, 1])
print(f"{CSort.sort()}")
