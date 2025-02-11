class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(lwr, hgr):
            while lwr < hgr:
                if s[lwr] != s[hgr]:
                    return False
                lwr += 1
                hgr -= 1
            return True

        lwr, hgr = 0, len(s) - 1
        while lwr < hgr:
            if s[lwr] != s[hgr]:
                return palindrome(lwr + 1, hgr) or palindrome(lwr, hgr - 1)
            lwr += 1
            hgr -= 1
        return True
