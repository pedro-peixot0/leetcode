class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0

        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        while left < right:
            if max_left <= max_right:
                left += 1
                current_left = height[left]

                if current_left > max_left:
                    max_left = current_left
                else:
                    water += max_left - current_left
            else:
                right -= 1
                current_right = height[right]

                if current_right > max_right:
                    max_right = current_right
                else:
                    water += max_right - current_right

        return water
