class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lft, rgt = 0, len(nums) - 1

        while lft <= rgt:
            mid = lft + (rgt - lft) // 2

            if nums[mid] < target:
                lft = mid + 1
            elif nums[mid] > target:
                rgt = mid - 1
            else:
                return mid

        return lft
