class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index = {}
        for i, c in enumerate(nums):
            if target - c in num_index:
                return [i, num_index[target-c]]
            num_index[c] = i
        return []   