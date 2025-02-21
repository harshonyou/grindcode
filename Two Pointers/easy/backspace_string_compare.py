class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def decode(ss):
            decoded = []
            idx = len(ss) - 1
            skips = 0

            while idx >= 0:
                if ss[idx] == "#":
                    skips += 1
                else:
                    if skips > 0:
                        skips -= 1
                    else:
                        decoded.append(ss[idx])
                idx -= 1

            return decoded

        return decode(s) == decode(t)
