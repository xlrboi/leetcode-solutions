class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        start = 0
        n = len(temperatures)
        ans = [0] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1] - i
            stk.append(i)

        return ans



