from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        c = Counter(nums)
        count = 0
        for key, val in c.items():
            if val > 1:
                n = val - 1
                count += (n * (n + 1)) // 2
        return count
