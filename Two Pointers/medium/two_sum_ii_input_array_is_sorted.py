class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lwr, hgr = 0, len(numbers) - 1

        while lwr < hgr:
            s = numbers[lwr] + numbers[hgr]
            if s < target:
                lwr += 1
            elif s > target:
                hgr -= 1
            else:
                return [lwr + 1, hgr + 1]

        return [-1, -1]
