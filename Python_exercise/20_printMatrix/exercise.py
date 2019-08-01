'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
class Solution(object):
    def printMatrix(self, matrix):
        if matrix == None:
            return None
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        while rows > start * 2 and cols > start * 2:
            self.printMatrixInCircle(matrix, cols, rows, start)
            start += 1
        print('')