class Solution:
    def func(self, index, nums, subset, ans):
        if index >= len(nums):
            ans.append(subset.copy())
            return
        subset.append(nums[index])

        self.func(index + 1, nums, subset, ans)
        subset.pop()
        self.func(index + 1, nums, subset, ans)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        self.func(0, nums, subset, ans)
        return ans