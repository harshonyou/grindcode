class Solution:
    def mySqrt(self, x: int) -> int:
        lwr, hgr = 0, x

        while lwr <= hgr:
            mid = lwr + (hgr - lwr) // 2
            val = mid * mid

            if val < x:
                lwr = mid + 1
            elif val > x:
                hgr = mid - 1
            else:
                return mid

        return hgr
