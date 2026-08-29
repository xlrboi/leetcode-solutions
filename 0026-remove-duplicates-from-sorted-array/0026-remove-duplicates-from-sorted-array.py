class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_set = set()
        index = 0
        for num in nums:
            if num not in my_set:
                my_set.add(num)
                nums[index] = num
                index += 1

        return index  
