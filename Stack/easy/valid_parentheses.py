from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        inverse = {"}": "{", "]": "[", ")": "("}

        stack = deque()

        for ch in s:
            if ch in inverse:
                if len(stack) != 0 and stack[-1] == inverse[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0
