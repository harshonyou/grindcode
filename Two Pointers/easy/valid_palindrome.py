class Solution:
    def isPalindrome(self, s: str) -> bool:
        lft, rgt = 0, len(s) - 1
        s = s.lower()

        while lft < rgt:
            if not s[lft].isalnum():
                lft += 1
            elif not s[rgt].isalnum():
                rgt -= 1
            else:
                if s[lft] != s[rgt]:
                    return False
                lft += 1
                rgt -= 1
        return True
