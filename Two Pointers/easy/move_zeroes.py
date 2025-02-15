class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow, fast = 0, 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while slow < len(nums):
            nums[slow] = 0
            slow += 1
