import math


class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()

        minima = math.inf
        left, right = 0, k - 1

        while right < len(nums):
            minima = min(minima, nums[right] - nums[left])
            left += 1
            right += 1

        return minima  # type: ignore
