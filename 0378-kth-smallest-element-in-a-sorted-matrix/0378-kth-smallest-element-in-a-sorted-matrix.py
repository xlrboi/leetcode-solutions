class Solution:
    def noOfElements(self, matrix, rows, cols, mid):
        row = rows - 1
        col = 0
        count = 0
        while(row >= 0 and col < cols):
            if matrix[row][col] <= mid:
                count += (row + 1)
                col += 1
            else:
                row -=1 

        return count

    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        low, high = matrix[0][0], matrix[rows - 1][cols - 1]
        res = -1
        while low <= high:
            mid = (low + high) // 2
            ans = self.noOfElements(matrix, rows, cols, mid)
            if ans < k:
                low = mid + 1
            else:
                res = mid
                high = mid - 1

        return res