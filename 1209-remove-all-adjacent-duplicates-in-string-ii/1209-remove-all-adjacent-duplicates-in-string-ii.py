class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for char in s:
            if stk and stk[-1][0] == char:
                stk[-1][1] += 1
            else:
                stk.append([char, 1])

            if stk[-1][1] == k:
                stk.pop()

        return "".join(char *count for char, count in stk)
