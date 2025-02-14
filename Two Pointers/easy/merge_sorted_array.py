class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        ptr1, ptr2 = 0, 0
        nums = []

        while ptr1 < m and ptr2 < n:
            if nums1[ptr1] <= nums2[ptr2]:
                nums.append(nums1[ptr1])
                ptr1 += 1
            else:
                nums.append(nums2[ptr2])
                ptr2 += 1

        if ptr1 < m:
            nums.extend(nums1[ptr1:])

        if ptr2 < n:
            nums.extend(nums2[ptr2:])

        for idx in range(len(nums1)):
            nums1[idx] = nums[idx]
