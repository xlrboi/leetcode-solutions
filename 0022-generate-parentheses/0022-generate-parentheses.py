class Solution:
    def func(self,index, brackets, result, total):
        if index >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return

        if total > len(brackets) // 2:
            return

        if total < 0:
            return 

        brackets[index] = "("
        Sum = total + 1
        self.func(index + 1, brackets, result, Sum)
        brackets[index] = ")"
        Sum = total - 1
        self.func(index + 1, brackets, result, Sum)

    def generateParenthesis(self, n: int) -> list[str]:
        brackets = [""] * ( n * 2 )
        result = []
        self.func(0, brackets, result, 0)
        return result
