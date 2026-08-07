class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        lst = []
        for i in range(n):
            if nums[i] != 0:
                lst.append(nums[i])

        n_lst = len(lst)
        for i in range(n_lst):
            nums[i] = lst[i]

        for i in range(n_lst,n):
            nums[i] = 0