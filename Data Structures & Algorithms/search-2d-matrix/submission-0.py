class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        t = 0
        b = len(matrix)

        while t < b:
            m = (t + b) // 2
            if target < matrix[m][-1]:
                b = m
            elif target > matrix[m][-1]:
                t = m + 1
            else:
                return True 

        if t == len(matrix):
            return False

        row = t

        l = 0
        r = len(matrix[row])

        while l < r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True

        return False