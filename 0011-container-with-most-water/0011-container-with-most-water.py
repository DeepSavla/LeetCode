class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        area=0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                curArea = min(height[i],height[j]) * (j-i)
                area = max(area, curArea)
        return area
        """
        i = 0
        j = len(height) - 1
        area = 0
        while j > i:
            area = max(area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area
        