class Solution(object):
    def minNumberInRotateArray(self, array):
        if len(array) == 0:
            return 0
        left, right = 0, len(array) - 1
        