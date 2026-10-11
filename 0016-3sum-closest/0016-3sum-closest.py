class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            low, high = i + 1, n - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]

                if abs(s - target) < abs(closest - target):
                    closest = s

                if s == target:
                    return s
                elif s > target:
                    high -= 1
                else:
                    low += 1

        return closest