class Solution:

    def rob(self, nums: list[int]) -> int:
        dp = [-1] * (len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i > 1:
                p = nums[i] + dp[i - 2]
            else:
                p = 0 + nums[i]

            np = 0 + dp[i - 1]
            dp[i] = max(p, np)
        return dp[len(nums) - 1]