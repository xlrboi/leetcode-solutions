class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(s, open, close):
            if len(s) == n * 2:
                res.append(s)
                return

            if open < n:
                helper(s + "(", open + 1, close)

            if close < open:
                helper(s + ")", open, close + 1)

        helper("", 0, 0)

        return res