from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1

        count = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequencies.items():
            count[freq].append(num)

        ans = []
        for idx in range(len(nums), -1, -1):
            for num in count[idx]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans
