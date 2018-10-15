class Solution:
    # low算法
    def threeSum(self, nums):
        nums.sort()
        result = []
        index, final = 0, len(nums)-1
        while final >= 2:
            for i in range(index+1, final):
                for j in range(i, final):
                    if nums[i-1] + nums[j] + nums[final] == 0:
                        result.append([nums[i-1], nums[j], nums[final]])
            final -= 1
        rr = []
        for item in result:
            if item not in rr:
                rr.append(item)
        print(len(rr))
        return rr

    def threeSum2(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left] + nums[right] < -nums[i]:
                        while left < right:
                            left += 1
                            if nums[left] > nums[left-1]:
                                break
                    else:
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right+1]:
                                break
        print(len(result))
        return result

    def threeSum3(self, nums):
        if not nums:
            return []
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        print(len(result))
        return result

    def threeSum4(self, nums):
        m = {}
        result = []
        # 记录每个数字出现的次数
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
        # 如果数组中出现三个以上0
        if 0 in m and m[0] >= 3:
            result.append([0, 0, 0])

        # 获取所有的数字，并排序
        keys = list(m.keys())
        keys.sort()
        keys_num = len(keys)
        if keys_num == 0:
            return []

        # a<b<c。a一定小于0，c一定大于0

        # a的取值范围
        end = bisect_left(keys, 0)  # a < 0
        begin = bisect_left(keys, -keys[-1] * 2)
        # when b == c, a + b + c = a + 2c <= a + 2*max_c;
        for i in range(begin, end):
            a = keys[i]

            # when a == b, then 2a = c
            if a != 0 and m[a] >= 2 and -2 * a in m:
                result.append([a, a, -2 * a])

            # b的取值范围
            # -a - b = c <= keys[-1] >>>> b >= -keys[-1] - a
            min_b = -keys[-1] - a
            # b<c >>>> a + 2b < a + b + c = 0 >>>> b < -a/2
            max_b = -a / 2

            b_begin = max(i + 1, bisect_left(keys, min_b))  # b的最小值
            b_end = bisect_right(keys, max_b)  # b的最大值
            # print('a = {}, {} <= b < {}, in [{}:{}]'.format(a, min_b, max_b, b_begin, b_end))
            for j in range(b_begin, b_end):
                b = keys[j]
                # print('key[{}] = {}, key[{}] = {}'.format(i, a, j, b))
                c = -a - b
                if c in m and b <= c:
                    if b < c or m[b] >= 2:
                        result.append([a, b, c])
        print(len(result))
        return result