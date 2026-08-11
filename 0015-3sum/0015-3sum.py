class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        result = set()
        n = len(arr)
        for i in range(n):
            my_set = set()
            for j in range(i+1, n):
                third = -(arr[i] + arr[j])
                if third in my_set:
                    temp = [arr[i], arr[j], third] 
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(arr[j])
        return [list(ans) for ans in result]      