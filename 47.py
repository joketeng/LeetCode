class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import Counter 
        num = Counter(nums)
        pertial = []
        self.helper(len(nums), [], num, pertial)
        return pertial
    
    def helper(self, add, partial, num, per):
        if add == 0:
            per.append(partial)
        for item in num:
            if num[item] > 0:
                num[item] -= 1
                self.helper(add-1, partial+[item], num, per)
                num[item] += 1