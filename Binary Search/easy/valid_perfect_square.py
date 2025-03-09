class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lwr, hgr = 0, num

        while lwr <= hgr:
            mid = lwr + (hgr - lwr) // 2
            val = mid * mid

            if val < num:
                lwr = mid + 1
            elif val > num:
                hgr = mid - 1
            else:
                return True

        return False
