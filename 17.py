class Solution:
    def letterCombinations(self, digits):
        if digits == '':
            return []
        iphones = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        results = [[]]
        for digit in digits:
            items = []
            for result in results:
                for iphone in iphones[digit]:
                    items.append(result + [iphone])
            results = items
        rrs = []
        for result in results:
           rrs.append(''.join(result))
        return rrs
    # return [''.join(result) for result in results]

    def __init__(self):
        self.digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if len(digits) == 0:
            return result

        def dfs(number, idx, sol):
            # 局部变量 py3
            nonlocal result
            if idx == len(number):
                result.append(sol)
                return
            for i in self.digits_map[number[idx]]:
                dfs(number, idx + 1, sol + i)

        dfs(digits, 0, '')
        return result