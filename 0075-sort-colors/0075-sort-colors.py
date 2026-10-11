class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0 
        twos = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        for i in range(zeros):
            nums[i] = 0
        for j in range(zeros, zeros + ones):
            nums[j] = 1
        for k in range(zeros + ones, len(nums)):
            nums[k] = 2