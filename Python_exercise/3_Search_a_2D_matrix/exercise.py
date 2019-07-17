#solution one
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        row, col = rows - 1, 0
        while row >= 0 and col <= cols - 1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False

#solution two
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
        	return False

        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
        	if matrix[row][col] == target:
        		return True
        	elif matrix[row][col] < target:
        		row += 1
        	else:
        		col -= 1
        return False