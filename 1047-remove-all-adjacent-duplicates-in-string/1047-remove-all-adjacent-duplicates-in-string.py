class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        res = ""
        for char in s:
            if stk and stk[-1] == char:
                stk.pop()
            else:
                stk.append(char)
        
        while stk:
            res += stk.pop()

        return res[::-1]