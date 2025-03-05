class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lwr = 0
        hgr = len(nums) - 1

        while lwr <= hgr:
            mid = lwr + (hgr - lwr) // 2

            if nums[mid] < target:
                lwr = mid + 1
            elif nums[mid] > target:
                hgr = mid - 1
            else:
                return mid

        return -1
