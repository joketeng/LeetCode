class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        for i, c in enumerate(nums):
            if(c >= target):
                return i
        return len(nums)





# er

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        
        if target > nums[j]:
            return j+1
        elif target < nums[i]:
            return i
        else:
            while i<=j:
                t = (i+j)//2
                if nums[t] < target:
                    i = t+1
                elif nums[t] > target:
                    j = t-1
                else:
                    return t
            return i