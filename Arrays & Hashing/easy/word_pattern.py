class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = list(pattern)
        ss = s.split(" ")
        detected_a = {}
        detected_b = {}

        if len(patterns) != len(ss):
            return False

        for idx, pattern in enumerate(patterns):
            if pattern in detected_a:
                if detected_a[pattern] != ss[idx]:
                    return False
            else:
                detected_a[pattern] = ss[idx]

        for idx, s in enumerate(ss):
            if s in detected_b:
                if detected_b[s] != patterns[idx]:
                    return False
            else:
                detected_b[s] = patterns[idx]

        return True
