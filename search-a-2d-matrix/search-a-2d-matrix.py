class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix) - 1
        while l<=r:
            m = (l + r)//2
            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        if l>r:
            return False
        l,r = 0,len(matrix[0])-1
        while l<=r:
            m = (l + r)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
