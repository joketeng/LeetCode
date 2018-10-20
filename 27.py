class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i, c in enumerate(nums):
            if c != val:
                nums[index] = c
                index += 1
        return index