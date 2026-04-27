class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        area = 0
        while left < right:
            if max_left > max_right:
                right -= 1
                max_right = max(height[right], max_right)
                area += max_right - height[right]
            else:
                left += 1
                max_left = max(height[left], max_left)
                area += max_left - height[left]
        return area