class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        lwr, hgr = 0, len(nums) - 1

        while lwr <= hgr:
            mid = lwr + (hgr - lwr) // 2

            if nums[mid] < 0:
                lwr = mid + 1
            else:
                hgr = mid - 1

        squares = []
        backward, forward = lwr - 1, lwr
        while backward >= 0 and forward < len(nums):
            neg = nums[backward] ** 2
            pos = nums[forward] ** 2

            if neg <= pos:
                squares.append(neg)
                backward -= 1
            else:
                squares.append(pos)
                forward += 1

        while backward >= 0:
            neg = nums[backward] ** 2
            squares.append(neg)
            backward -= 1

        while forward < len(nums):
            pos = nums[forward] ** 2
            squares.append(pos)
            forward += 1

        return squares
