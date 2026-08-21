class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        maxi = 0
        left = 0
        right = 0
        my_dict = dict()
        n = len(nums)
        while right < n:
            my_dict[nums[right]] = my_dict.get(nums[right], 0) + 1
            if len(my_dict) > 2:
                my_dict[nums[left]] -= 1
                if my_dict[nums[left]] == 0:
                    del(my_dict[nums[left]])
                left += 1
            if len(my_dict) <= 2:
                maxi = max(maxi, right - left + 1)
            right += 1
        return maxi 