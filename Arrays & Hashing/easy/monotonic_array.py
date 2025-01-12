class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        asc = nums[-1] >= nums[0]

        for idx in range(1, len(nums)):
            if asc:
                if nums[idx - 1] > nums[idx]:
                    return False
            else:
                if nums[idx - 1] < nums[idx]:
                    return False

        return True
