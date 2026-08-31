class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        dict1 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1

        sorted_char = sorted(dict1.items(), key = lambda x : (-x[1], x[0]))
        for char, freq in sorted_char:
            result += (char * freq)

        return result

