from collections import deque


class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque()

        for ch in s:
            if len(stack) != 0:
                last = stack[-1]
                if last != ch and (last == ch.upper() or last == ch.lower()):
                    stack.pop()
                    continue
            stack.append(ch)

        return "".join(stack)
