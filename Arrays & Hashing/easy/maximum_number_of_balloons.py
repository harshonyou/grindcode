import math
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        possible = math.inf
        t = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        for ch, val in t.items():
            print(c[ch], ch, val)
            possible = min(possible, c[ch] // val)

        return possible  # type: ignore
