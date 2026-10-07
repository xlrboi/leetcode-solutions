class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return abs(nums[0])
        best_sum_pos = nums[0]
        best_sum_neg = nums[0]
        sumi_pos = nums[0]
        sumi_neg = nums[0]
        res = nums[0]
        for i in range(1, n):
            v1 = best_sum_pos + nums[i]
            v2 = best_sum_neg + nums[i]
            v3 = nums[i]

            best_sum_pos = max(v1, v3)
            sumi_pos = max(sumi_pos, best_sum_pos)
            best_sum_neg = min(v2, v3)
            sumi_neg = min(sumi_neg, best_sum_neg)

            res = max(abs(sumi_pos), abs(sumi_neg))

        return res 