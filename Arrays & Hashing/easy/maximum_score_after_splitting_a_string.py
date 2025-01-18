class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for ch in s:
            if ch == "1":
                ones += 1

        zeroes = 0
        maxima = 0
        for idx in range(len(s) - 1):
            if s[idx] == "0":
                zeroes += 1
            else:
                ones -= 1

            maxima = max(maxima, (zeroes + ones))

        return maxima
