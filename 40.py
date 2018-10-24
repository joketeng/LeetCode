class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.sum2(candidates, 0, target, [], res)
        return res
    
    def sum2(self, nums, next, target, partial, result):
        if target == 0:
            result.append(partial)
            return 
        if len(nums) == next:
            return 
        for i in range(next, len(nums)):
            if i > next and nums[i] == nums[i-1]:
                continue
            if target - nums[i] < 0:
                break    
            self.sum2(nums, i+1 , target-nums[i], partial+[nums[i]], result)