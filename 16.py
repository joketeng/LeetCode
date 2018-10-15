class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        if result >= target:
            return result
        for i in range(len(nums) - 2):
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum == target:
                        return sum
                    if abs(sum - target) < abs(result - target):
                        result = sum
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
        return result

    def threeSumClosest2(self, nums, target):
        result = []
        nums.sort()
        for i, num in enumerate(nums[0:-2]):
            left = i+1
            right = len(nums)-1
            if nums[left] + nums[left+1] + num > target:
                result.append(nums[left] + nums[left+1] + num)
            elif nums[right] + nums[right-1] + num < target:
                result.append(nums[right] + nums[right-1] + num)
            else:
                while left < right:
                    result.append(nums[left] + nums[right] + num)
                    if nums[left] + nums[right] + num < target:
                        left += 1
                    elif nums[left] + nums[right] + num > target:
                        right -= 1
                    else:
                        return nums[left] + nums[right] + num
        # ¹Ø¼ü´Ê£ºlambda ÄäÃûº¯Êı
        result.sort(key=lambda x: abs(x - target))
        return result[0]