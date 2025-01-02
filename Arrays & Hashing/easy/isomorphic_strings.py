class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = dict(), dict()
        for idx in range(len(s)):
            _s, _t = s[idx], t[idx]

            if _s in m1 and m1[_s] != _t:
                return False

            if _t in m2 and m2[_t] != _s:
                return False

            m1[_s] = _t
            m2[_t] = _s

        return True
