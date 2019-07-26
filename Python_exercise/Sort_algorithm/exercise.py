class Solution(object):
    def bubbleSort(self, alist):
        for i in range(len(alist)-1, 0, -1):
            for j in range(i):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
        return alist

    def selectionSort(self, alist):
        min_index = 0
        for i in range(1, len(alist)):
            j = i
            if alist[j] < alist[min_index]:
                min_index = j
            alist[min_index], alist[j] = alist[j], alist[min_index]
        return alist
    
    def insertSort(self, alist):
        for i in range(1, len(alist)):
            for j in range(i, 0 ,-1):
                if alist[j] < alist[j-1]:
                    alist[j-1], alist[j] = alist[j], alist[j-1]
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
        while gap >0:
            for i in range(gap, len(alist)):
                j = i
                if j >= gap and alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    j -= gap
                gap //= 2
        return alist
    
    def quickSort(self, alist, start, last):
        if start >= last:
            return None
        low = start
        high = last
        mid = alist[start]
        while low < high:
            while low < high and alist[high] >= mid:
                high -= 1
            alist[low] = alist[high]
            while low < high and alist[low] < mid:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid
        self.quickSort(alist, start, low-1)
        self.quickSort(alist, low+1, high)
        return alist
            

    def mergeSort(self, alist):
        if len(alist) <= 1:
            return alist
        mid = len(alist) // 2
        self.mergeSort(alist[:mid])
        self.mergeSort(alist[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        left_pointer, right_pointer = 0, 0
        result = []
        while left_pointer <= len(left) and right_pointer <= len(right):
            if left[left_pointer] < right[right_pointer]:
                result.append(left_pointer)
                left_pointer += 1
            else:
                result.append(right_pointer)
                right_pointer += 1
        result += left[left_pointer:]
        result += right[right_pointer:]
        return result 

s = Solution()
