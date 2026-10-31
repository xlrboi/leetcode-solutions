class Solution:
    def fib(self, n: int) -> int:
        prev2 = 0
        prev = 1
        if n == 0:
            return prev2

        elif n == 1:
            return prev
        
        else:
            for _ in range(2, n + 1):
                curr = prev + prev2
                prev2 = prev
                prev = curr

        return prev