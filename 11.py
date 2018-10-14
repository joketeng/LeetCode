class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea, index, final = 0, 0, len(height)-1
        while(index < final):
            maxarea = max(maxarea, min(height[index], height[final]) * (final - index))
            if height[index] < height[final]:
                index += 1
            else:
                final -= 1
        return maxarea