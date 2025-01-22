import math


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        s = (n * (n + 1)) // 2
        c = sum(nums)

        unique = set()
        dupe = math.inf
        for num in nums:
            if num in unique:
                dupe = num
                break
            else:
                unique.add(num)

        return [dupe, s - c + dupe]  # type: ignore
