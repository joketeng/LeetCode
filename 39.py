class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.sum(candidates, 0, target, [], results)
        return results
        
    def sum(self, nums, next, target, partial, results):
        if target == 0:
            results.append(partial)
            return 
        if next == len(nums):
            return 
        i = 0
        while target-i*nums[next] >=0:
            self.sum(nums,next+1, target-i*nums[next], partial+[nums[next]]*i, results)
            i+=1
        