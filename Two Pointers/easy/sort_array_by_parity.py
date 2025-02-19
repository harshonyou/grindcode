class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        isEven = lambda x: x % 2 == 0
        left, right = 0, len(nums) - 1

        while left < right:
            if isEven(nums[left]):
                left += 1
            if not isEven(nums[right]):
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]

        return nums
