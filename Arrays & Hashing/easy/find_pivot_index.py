class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right = sum(nums)
        left = 0

        for idx in range(len(nums)):
            if idx > 0:
                left += nums[idx - 1]
            right -= nums[idx]
            if left == right:
                return idx

        return -1
