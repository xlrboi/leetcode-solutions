class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        tot_sub = 2**n
        result = []
        for num in range(0, tot_sub):
            lst = []
            for i in range(n):
                if(num & (1<<i)) != 0:
                    lst.append(nums[i])
            result.append(lst)

        return result