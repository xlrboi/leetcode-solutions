class Solution:

    def rob(self, nums: list[int]) -> int:
        prev = nums[0]
        prev2 = nums[0]
        for index in range(1, len(nums)):
            if index > 1:
                p = nums[index] + prev2
            else:
                p = nums[index] 

            np = 0 + prev 

            curr = max(p, np)
            prev2 = prev
            prev = curr

        return prev 