class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        neg = []
        pos = []
        res = []
        for num in nums:
            if num >= 0:
                pos.append(num ** 2)
            else:
                neg.append(num ** 2)

        n = len(pos)
        m = len(neg) 
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if pos[i] > neg[j]:
                res.append(neg[j])
                j -= 1
            else:
                res.append(pos[i])
                i += 1
            
            

        while i < n:
            res.append(pos[i])
            i += 1

        while j >= 0:
            res.append(neg[j])
            j -= 1    

        return res