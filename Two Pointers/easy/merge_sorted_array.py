class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        ptr1, ptr2 = m - 1, n - 1
        ptr = m + n - 1

        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            ptr -= 1

        while ptr2 >= 0:
            nums1[ptr] = nums2[ptr2]
            ptr2 -= 1
            ptr -= 1
