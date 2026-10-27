class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0 
        count = 1
        check = 1
        while check < len(nums):
            if nums[check] == nums[check - 1]:
                check += 1
                continue
            else:
                start += 1
                nums[start] = nums[check]
                check += 1
        return start + 1