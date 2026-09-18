class Solution:
    def solve(self, index, nums, dp):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0
        if dp[index] != -1:
            return dp[index]


        p = nums[index] + self.solve(index - 2, nums, dp)
        np = 0 + self.solve(index - 1, nums, dp)
        dp[index] = max(p, np)
        return dp[index]

    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[-]
        dp = [-1] * (n - 1)
        ans1 = self.solve(n - 2, nums[: n - 1], dp)
        dp = [-1] * (n - 1)
        ans2 = self.solve(n - 2, nums[1:], dp)
        return max(ans1, ans2)
        