class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        base = strs[0]
        for i in range(len(base)):
            for word in strs:
                if i == len(word) or word[i] != base[i]:
                    return result 
            result += base[i]

        return result 