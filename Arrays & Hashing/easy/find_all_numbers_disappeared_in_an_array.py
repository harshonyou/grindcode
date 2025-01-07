class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s = set(nums)
        arr = []

        for idx in range(1, len(nums) + 1):
            if idx not in s:
                arr.append(idx)

        return arr
