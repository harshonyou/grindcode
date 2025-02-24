class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for idx, num in enumerate(nums):
            if num > 0:
                break
            if idx > 0 and num == nums[idx - 1]:
                continue

            target = -num
            lwr, hgr = idx + 1, len(nums) - 1
            while lwr < hgr:
                s = nums[lwr] + nums[hgr]
                if s < target:
                    lwr += 1
                elif s > target:
                    hgr -= 1
                else:
                    ans.append([num, nums[lwr], nums[hgr]])
                    lwr += 1
                    hgr -= 1
                    while nums[lwr] == nums[lwr - 1] and lwr < hgr:
                        lwr += 1

        return ans
