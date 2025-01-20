class Solution:
    def minOperations(self, s: str) -> int:
        def helper(toggle):
            mismatches = 0
            for ch in s:
                if toggle and ch != "1":
                    mismatches += 1
                if not toggle and ch != "0":
                    mismatches += 1
                toggle = not toggle
            return mismatches

        return min(helper(0), helper(1))
