class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ori_sum = int((n * (n+1))/2)
        sum = 0
        for i in range(n):
            sum += nums[i]

        return ori_sum - sum
