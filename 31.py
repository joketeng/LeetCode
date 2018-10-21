class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums and len(nums) == 1:
            return 
        i = len(nums) - 2
        # �Ӻ���Ѱ�ҵ�һ���������
        while nums[i] >= nums[i+1] and i >= 0:
            i -= 1
        # Ѱ�Һ����һ���Ƚ�����С������ǰ����������н���
        if i != -1:
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left = i+1
        right = len(nums)-1
        # �������������
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            right -= 1
            left += 1
            