class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        for _ in range(k):
            e = nums.pop()
            nums.insert(0,e)