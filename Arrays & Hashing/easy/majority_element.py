class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        runningMajor = nums[0]
        runningFreq = 1
        ptr = 1

        while ptr < len(nums):
            num = nums[ptr]

            if num == runningMajor:
                runningFreq += 1
            else:
                runningFreq -= 1

            if runningFreq <= 0:
                runningMajor = num
                runningFreq = 1

            ptr += 1

        return runningMajor
