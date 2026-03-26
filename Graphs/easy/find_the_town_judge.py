from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for trustor, trusted in trust:
            delta[trustor] -= 1
            delta[trusted] += 1

        for idx in range(1, n + 1):
            if delta[idx] == n - 1:
                return idx

        return -1
