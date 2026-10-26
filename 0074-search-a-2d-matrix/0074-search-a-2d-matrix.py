class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low_r = 0
        high_r = rows - 1
        ans = -1
        while low_r <= high_r:
            mid_r = (low_r + high_r) // 2
            if matrix[mid_r][0] > target:
                high_r = mid_r - 1
            else:
                ans = mid_r
                low_r = mid_r + 1

        if ans == -1:
            return False


        low_c = 0
        high_c = cols - 1
        while low_c <= high_c:
            mid_c = (low_c + high_c) // 2
            if matrix[ans][mid_c] == target:
                return True
            elif matrix[ans][mid_c] > target:
                high_c = mid_c - 1
            else:
                low_c = mid_c + 1

        return False
