from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        m = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord("a")] += 1

            m[tuple(count)].append(s)

        return list(m.values())
