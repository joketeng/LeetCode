class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {')':'(', ']':'[','}':'{'}
        for i in s:
            if i in match.values():
                stack.append(i)
            elif i in match.keys():
                if stack==[] or stack.pop() != match[i]:
                    return False
            else:
                return False
        return stack == []