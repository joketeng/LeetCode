class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums and len(nums) == 1:
            return 
        i = len(nums) - 2
        # 从后面寻找第一个降序的数
        while nums[i] >= nums[i+1] and i >= 0:
            i -= 1
        # 寻找后面第一个比降序数小的数的前面的数，进行交换
        if i != -1:
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left = i+1
        right = len(nums)-1
        # 将后面的数反序
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            right -= 1
            left += 1
            