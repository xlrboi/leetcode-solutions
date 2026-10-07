class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        mini = nums[0]
        maxi = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            v1 = mini * nums[i]
            v2 = maxi * nums[i]
            v3 = nums[i]
            maxi = max(v3, max(v1, v2))
            mini = min(v3, min(v1, v2))
            res = max(res, max(maxi, mini))

        return res 