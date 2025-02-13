class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        ans = []
        idx = 0

        while idx < len1 and idx < len2:
            ans.append(word1[idx])
            ans.append(word2[idx])
            idx += 1

        while idx < len1:
            ans.append(word1[idx])
            idx += 1

        while idx < len2:
            ans.append(word2[idx])
            idx += 1

        return "".join(ans)
