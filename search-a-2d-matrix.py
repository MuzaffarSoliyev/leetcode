class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][cols - 1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, cols - 1
        row_m = (top + bot) // 2
        while l <= r:
            col_m = (l + r) // 2
            if matrix[row_m][col_m] < target:
                l = col_m + 1
            elif matrix[row_m][col_m] > target:
                r = col_m - 1
            else:
                return True
        return False
