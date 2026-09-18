class Solution:
    def func(self, index, nums, dp):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        p = nums[index] + self.func(index - 2, nums, dp)
        np = 0 + self.func(index - 1, nums, dp)
        dp[index] = max(p,np)

        return dp[index]

    def rob(self, nums: list[int]) -> int:
        dp = [-1] * (len(nums))
        return self.func(len(nums) - 1, nums, dp)