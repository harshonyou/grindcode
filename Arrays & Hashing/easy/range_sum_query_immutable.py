class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [nums[0]] * len(nums)
        self.postfix = [nums[-1]] * len(nums)
        self.sum = sum(nums)

        for idx in range(1, len(nums)):
            self.prefix[idx] = self.prefix[idx - 1] + nums[idx]

        for idx in range(len(nums) - 1 - 1, -1, -1):
            self.postfix[idx] = self.postfix[idx + 1] + nums[idx]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] + self.postfix[left] - self.sum
