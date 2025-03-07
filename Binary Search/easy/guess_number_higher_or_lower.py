def guess(num: int) -> int:
    raise NotImplementedError


class Solution:
    def guessNumber(self, n: int) -> int:
        lwr, hgr = 1, n

        while lwr <= hgr:
            mid = lwr + (hgr - lwr) // 2
            val = guess(mid)
            if val == 1:
                lwr = mid + 1
            elif val == -1:
                hgr = mid - 1
            else:
                return mid

        return -1
