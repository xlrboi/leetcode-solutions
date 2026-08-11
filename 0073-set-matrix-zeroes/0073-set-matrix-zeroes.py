class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r, c= len(matrix), len(matrix[0])
        rowtrack = [0 for _ in range (r)]
        coltrack = [0 for _ in range (c)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1

        for i in range(r):
            for j in range(c):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0