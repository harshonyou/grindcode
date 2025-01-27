class Solution:
    def specialArray(self, nums: list[int]) -> int:
        count = [0] * (len(nums) + 1)
        for num in nums:
            idx = min(num, len(nums))
            count[idx] += 1

        total = 0
        for idx in range(len(nums), -1, -1):
            total += count[idx]
            if total == idx:
                return idx

        return -1
