class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lst1 = []
        lst2 = []
        n = len(nums)
        for i in range(n):
            if nums[i] >= 0:
                lst1.append(nums[i])
            else:
                lst2.append(nums[i])

        for i in range(len(lst1)):
            nums[2*i] = lst1[i]
            nums[(2*i) + 1] = lst2[i]

        return nums

