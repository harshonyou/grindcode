class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]]
        for idx in range(1, len(nums)):
            prefix.append(prefix[idx - 1] * nums[idx])

        postfix = 1
        for idx in range(len(nums) - 1, 0, -1):
            prefix[idx] = prefix[idx - 1] * postfix
            postfix *= nums[idx]
        prefix[0] = postfix

        return prefix
