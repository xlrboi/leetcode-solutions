class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        for i in range(len(s)):
            my_set = set()
            for j in range(i,len(s)):
                if s[j] in my_set:
                    break
                maxi = max(maxi, j-i+1)
                my_set.add(s[j])
        return maxi