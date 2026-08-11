class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        total = n*m
        counter = 0
        rowstart = 0
        rowend = n-1
        colstart = 0
        colend = m-1
        while counter < total:
            for i in range(colstart, colend+1):
                ans.append(matrix[rowstart][i])
                counter+=1
            rowstart+=1       
            if counter == total:
                break

            for i in range(rowstart, rowend+1):
                ans.append(matrix[i][colend])
                counter+=1
            colend-=1
            if counter == total:
                break

            for i in range(colend, colstart-1, -1):
                ans.append(matrix[rowend][i])
                counter+=1
            rowend-=1
            if counter ==total:
                break

            for i in range(rowend, rowstart-1, -1):
                ans.append(matrix[i][colstart])
                counter+=1
            colstart+=1
            if counter  == total:
                break
        return ans