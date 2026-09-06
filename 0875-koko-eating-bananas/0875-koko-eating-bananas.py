import math

class Solution:
    def calculatetotalhours(self, piles, speed):
        total = 0
        for bananas in piles:
            total += math.ceil(bananas/speed)
        return total


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpile = max(piles)
        low, high = 1, maxpile
        ans = maxpile
        while low <= high:
            mid = (low + high)//2
            total = self.calculatetotalhours(piles, mid)

            if total <= h:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans
    
