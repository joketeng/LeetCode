class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums)<=3:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1
        if target >= nums[0]:
            i = 0
            while i<len(nums) and nums[0] <= nums[i]:
                if nums[i] == target:
                    return i
                i +=1
            return -1
        if target <= nums[-1]:
            i = len(nums)-2
            if target == nums[-1]:
                return len(nums)-1
            while i>=0 and nums[i] < nums[i+1]:
                if target == nums[i]:
                    return i
                if target < nums[i]:
                    i -= 1
                else:
                    return -1
        return -1





# er




class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1