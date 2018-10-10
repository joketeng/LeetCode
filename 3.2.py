class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        begin = res = 0
        for i , ch in enumerate(s):
            if ch not in d or begin > d[ch]:
                curr = i - begin +1
                # current length
                res = curr if curr > res else res
            else :
                begin = d[ch] + 1
            d[ch] = i
        return res   