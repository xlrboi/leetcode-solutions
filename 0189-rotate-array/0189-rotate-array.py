class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k = k%l
        nums[:] = nums[l-k:] + nums[:l-k]