class Solution:
    def merge(self, list1, list2):
        ptr1, ptr2 = 0, 0
        len1, len2 = len(list1), len(list2)
        merged = []

        while ptr1 < len1 and ptr2 < len2:
            if list1[ptr1] <= list2[ptr2]:
                merged.append(list1[ptr1])
                ptr1 += 1
            else:
                merged.append(list2[ptr2])
                ptr2 += 1

        if ptr1 < len1:
            merged += list1[ptr1:]
        if ptr2 < len2:
            merged += list2[ptr2:]

        return merged

    def sort(self, nums):
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        return self.merge(self.sort(nums[:mid]), self.sort(nums[mid:]))

    def sortArray(self, nums: list[int]) -> list[int]:
        return self.sort(nums)
