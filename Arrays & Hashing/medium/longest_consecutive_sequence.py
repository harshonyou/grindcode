from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        m = defaultdict(int)
        maxima = 0

        for num in nums:
            if not m[num]:
                m[num] = m[num - 1] + m[num + 1] + 1
                m[num - m[num - 1]] = m[num]
                m[num + m[num + 1]] = m[num]
                maxima = max(maxima, m[num])
        return maxima
