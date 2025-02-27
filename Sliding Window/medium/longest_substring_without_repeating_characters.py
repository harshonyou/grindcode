class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        l, r = 0, 0
        maxima = 0

        for idx in range(len(s)):
            if s[idx] not in track:
                track.add(s[idx])
                r += 1
                maxima = max(maxima, r - l)
            else:
                while s[l] != s[idx]:
                    track.remove(s[l])
                    l += 1
                l += 1
                r += 1

        return maxima
