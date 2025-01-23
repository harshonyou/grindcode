class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}

        for idx in range(len(s)):
            ch = s[idx]

            if ch in m:
                m[ch] = -1
            else:
                m[ch] = idx

        for _, val in m.items():
            if val != -1:
                return val

        return -1
