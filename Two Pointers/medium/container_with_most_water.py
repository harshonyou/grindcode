class Solution:
    def maxArea(self, height: list[int]) -> int:
        lft, rgt = 0, len(height) - 1
        maxima = 0

        while lft < rgt:
            maxima = max(maxima, min(height[lft], height[rgt]) * (rgt - lft))
            if height[lft] <= height[rgt]:
                lft += 1
            else:
                rgt -= 1

        return maxima
