class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = True

        for num in nums:
            if num == 0:
                return 0

            if num < 0:
                sign = not sign

        if sign:
            return 1
        return -1
