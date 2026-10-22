class Solution:
    def helper(self, index, digits, current, result, mapping):
        if index == len(digits):
            result.append("".join(current))
            return
        letters = mapping[digits[index]]
        for ch in letters:
            current.append(ch)
            self.helper(index + 1, digits, current, result, mapping)
            current.pop()

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        result = []
        self.helper(0, digits, [], result, mapping)
        return result