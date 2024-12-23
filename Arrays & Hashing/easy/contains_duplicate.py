class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)
