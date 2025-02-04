class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        print(s)
        ans = []
        idx = 0
        while idx < len(s):
            tag = idx
            while s[tag] != "#":
                tag += 1
            count = int(s[idx:tag])
            ans.append(s[tag + 1 : tag + 1 + count])
            idx = tag + count + 1
        return ans
