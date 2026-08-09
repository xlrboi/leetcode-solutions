class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        # s = list(s)
        s = s[::-1]
        return " ".join(s)       