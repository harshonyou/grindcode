import math


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        prev = math.inf

        while fast < len(nums):
            if prev != nums[fast]:
                nums[slow] = nums[fast]
                prev = nums[fast]
                slow += 1
            fast += 1

        return slow
