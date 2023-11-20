class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        l, r = 0 , len(height) - 1
        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                l +=1
            else:
                area = height[r] * (r - l)
                r -=1

            max_area = max(max_area, area)

        return max_area
