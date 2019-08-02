class Solution(object):
    def bubbleSort(self, alist):
        for i in range(len(alist)-1, 0, -1):
            for j in range(i):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
        return alist

    def selectionSort(self, alist):
        for i in range(len(alist)-1):
            min_index = i
            for j in range(i+1, len(alist)):
                if alist[min_index] > alist[j]:
                    min_index = j
                alist[min_index], alist[j] = alist[j], alist[min_index]
        return alist

    def insertSort(self, alist):
        for i in range(1, len(alist)):
            for j in range(i, 0, -1):
                if alist[j] < alist[j-1]:
                    alist[j], alist[j-1] = alist[j-1], alist[j]
        return alist

    def insertSort2(self, alist):
        for i in range(1, len(alist)):
            j = i
            while j > 0:
                if alist[j] < alist[j-1]:
                    alist[j], alist[j-1] = alist[j-1], alist[j]
                    j -= 1
                else:
                    break
        return alist
                    
                    

    def shellSort(self, alist):
        gap = len(alist) // 2
        while gap > 0:
            for i in range(gap, len(alist)):
                j = i
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
            gap //= 2
        return alist


    def quickSort(self, alist, first, last):
        if first >= last:
            return None
        slow = first
        high = last
        mid = alist[first]
        while slow < high:
            while slow < high and alist[high] >= mid:
                high -= 1
            alist[slow] = alist[high]
            while slow < high and alist[slow] < mid:
                slow += 1
            alist[high] = alist[slow]
        alist[slow] = mid
        self.quickSort(alist, first, slow-1)
        self.quickSort(alist, slow+1, last)
        return alist


    def mergeSort(self, alist):
        mid = len(alist) // 2
        if len(alist) <= 1:
            return alist
        self.mergeSort(alist[:mid])
        self.mergeSort(alist[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        left_pointer = right_pointer = 0
        result = []
        while left_pointer < len(alist) and right_pointer < len(alist):
            result.append(alist[left_pointer])
            left_pointer += 1
        else:
            result.append(alist[right_pointer])
            right_pointer += 1
        result += alist[left_pointer:]
        result += alist[right_pointer:]
        return result
        


