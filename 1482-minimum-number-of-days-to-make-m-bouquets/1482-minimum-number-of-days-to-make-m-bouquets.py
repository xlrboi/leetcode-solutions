class Solution:
    def possible(self, bloomDay, day, m , k):
        counter = 0
        n = len(bloomDay)
        bouquets= 0
        for i in range(n):
            if bloomDay[i] <= day:
                counter += 1
            else:
                bouquets += (counter//k)
                counter = 0

        bouquets += (counter//k)
        return bouquets
        

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if len(bloomDay) < ( m * k ):
            return -1 

        mini = min(bloomDay)
        maxi = max(bloomDay)
        ans = -1

        while mini <= maxi:
            mid = (mini + maxi) // 2
            poss = self.possible(bloomDay, mid, m, k)
            if poss >= m:
                ans = mid
                maxi = mid - 1
            else:
                mini = mid + 1

        return ans