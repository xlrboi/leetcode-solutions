class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        res = list(dict.fromkeys(nums))

        count = 1
        max_count = 1
        i = 0

        while i < len(res) - 1:
            if res[i + 1] == res[i] + 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

            i += 1

        return max_count