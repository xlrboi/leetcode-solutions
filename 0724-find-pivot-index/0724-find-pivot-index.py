class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        sumi = sum(nums)
        left = 0
        for i in range(n):
            right = sumi - left - nums[i]

            if left == right:
                return i 

            left += nums[i]

        return -1 

