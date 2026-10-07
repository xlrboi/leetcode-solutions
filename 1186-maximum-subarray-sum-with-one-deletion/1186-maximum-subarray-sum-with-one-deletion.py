class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]

        max_no_dlt = arr[0]
        max_one_dlt = arr[0]
        ans = arr[0]
        for i in range(1, n):
            prev_no_dlt = max_no_dlt
            max_no_dlt = max(max_no_dlt + arr[i], arr[i])
            max_one_dlt = max(max_one_dlt + arr[i], prev_no_dlt)
            ans = max(ans, max(max_no_dlt, max_one_dlt))

        return ans