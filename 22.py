class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate([], n, n, result)
        return result
        
    def generate(self,partial, left , right, result):
        # 当左右括号数都为零时，将partial元祖添加至result中
        if left == 0 and right == 0:
            result.append(''.join(partial))
        # 当指标性左括号数不为零时，元祖中添加（，并且左括号是减一
        if left != 0:
            self.generate(partial + ['('], left-1, right, result)
        # 当左括号数小于右括号数时，元祖添加），并且右括号数减一
        if left < right:
            self.generate(partial + [')'], left, right-1, result)