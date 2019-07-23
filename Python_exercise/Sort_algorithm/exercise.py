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
            if alist[j] < alsit[min_index]:
                min_index = j
            alist[min_index], alist[j] = alist[j], alist[min_index]
        return alist
    
    def insertSort(self, alist):
        pass

            

        


    def shellSort(self, alist):
        pass
    
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
            while low < hign and alist[low] < mid:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid
        self.quickSort(alist, start, low-1)
        self.quickSort(alist, low+1, high)
        return alist
            

    def mergeSort(self, alist):
        pass

s = Solution()
