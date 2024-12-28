class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = dict()

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], idx]

            hashmap[num] = idx

        return [-1, -1]
