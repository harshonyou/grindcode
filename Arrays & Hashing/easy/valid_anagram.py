from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = defaultdict(int)
        for idx in range(len(s)):
            hashmap[s[idx]] += 1
            hashmap[t[idx]] -= 1

        for _, val in hashmap.items():
            if val != 0:
                return False

        return True
