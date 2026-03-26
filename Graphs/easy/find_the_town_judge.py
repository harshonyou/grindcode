from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return n

        judge = defaultdict(lambda: True)
        score = defaultdict(int)

        for [x, y] in trust:
            judge[x] = False
            score[y] += 1

        for j, s in score.items():
            if s == (n - 1) and judge[j]:
                return j

        return -1
