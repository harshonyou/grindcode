class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow_ptr, fast_ptr = 0, 0

        while fast_ptr < len(nums):
            if nums[fast_ptr] != val:
                nums[slow_ptr] = nums[fast_ptr]
                slow_ptr += 1
            fast_ptr += 1

        return slow_ptr
