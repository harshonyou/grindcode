class Solution:
    def sortColors(self, nums: list[int]) -> None:
        frequencies = {0: 0, 1: 0, 2: 0}
        for num in nums:
            frequencies[num] += 1
        idx = 0
        for i in range(3):
            for _ in range(frequencies[i]):
                nums[idx] = i
                idx += 1
