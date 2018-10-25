class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        return self.conbin(nums, 0)
        
        
    def conbin(self, nums, next):
        res = []
        if next == len(nums):
            res.append(nums[:])
        for i in range(next, len(nums)):
            nums[i], nums[next] = nums[next], nums[i]
            res += self.conbin(nums, next+1)
            nums[i], nums[next] = nums[next], nums[i]
        return res
            
            