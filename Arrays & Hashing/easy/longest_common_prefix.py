class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        possible = strs[0]
        current = ""
        idx = 0

        while idx < len(possible):
            for s in strs:
                if len(s) <= idx or s[idx] != possible[idx]:
                    return current
            current += possible[idx]
            idx += 1

        return current
