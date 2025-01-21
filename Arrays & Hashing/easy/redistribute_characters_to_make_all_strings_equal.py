from collections import Counter, defaultdict


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        m = defaultdict()
        c = Counter()
        n = len(words)

        for word in words:
            c += Counter(word)

        print(c)

        for key, val in c.items():
            if val % n != 0:
                return False

        return True
