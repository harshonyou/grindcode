import math


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = -math.inf
        running_num = ""
        running_freq = 0

        for char in num:
            if char == running_num:
                running_freq += 1

                if running_freq >= 3:
                    largest = max(int(running_num * 3), largest)
            else:
                running_num = char
                running_freq = 1

        if largest == -math.inf:
            return ""
        return f"{largest:03}"
