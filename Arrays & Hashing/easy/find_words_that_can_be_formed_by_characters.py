class Solution:
    def check(self, word, available):
        check = [0] * 26
        for ch in word:
            idx = ord(ch) - ord("a")
            check[idx] += 1
            if check[idx] > available[idx]:
                return False

        return True

    def countCharacters(self, words: list[str], chars: str) -> int:
        ans = 0
        available = [0] * 26

        for ch in chars:
            available[ord(ch) - ord("a")] += 1

        for word in words:
            if self.check(word, available):
                ans += len(word)

        return ans
