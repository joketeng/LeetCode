class Solution:
    ELEMENTS = 4

    def fourSum(self, nums, target):
        results = []
        self.n_sum(sorted(nums), target, [], self.ELEMENTS, results)
        print(len(results))
        return results

    def n_sum(self, nums, target, partial, n, results):
        # target为目标数的差值，partial是部分的list存放results的元祖
        if len(nums) < n or target > nums[-1]*n or target < nums[0]*n:
            return []
        # 当n为2调用正常的比较得到对应的元素组合
        if n == 2:
            left = 0
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append(partial + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[right] == nums[right+1] and right > left:
                        right -= 1
                    while nums[left] == nums[left-1] and right > left:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        # 当n不为2时(可以说是大于2)
        else:
            for i in range(len(nums)-n+1):
                # 总是将第一个数字放进partial元祖中，在后期调用中判断该元素是否重复
                if i == 0 or nums[i] != nums[i-1]:
                    # 将nums列表前调，抛出的元素与target相减得到更新后的目标值，partial元祖中再次存入该元素，所需要的元祖元素个数减一
                    self.n_sum(nums[i+1:], target-nums[i], partial+[nums[i]], n-1, results)