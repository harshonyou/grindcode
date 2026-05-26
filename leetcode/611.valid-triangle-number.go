package main

import (
	"slices"
)

// @leet start
func triangleNumber(nums []int) int {
	// valid triangle -> a + b > c
	// sort the list so, idx0 < idx1 < ... < idxN
	// do a backward loop for idx
	// search for any left and right that sums larger
	var count int
	slices.Sort(nums)
	n := len(nums)

	for idx := n - 1; idx >= 2; idx-- {
		left := 0
		right := idx - 1

		for left < right {
			if nums[left]+nums[right] > nums[idx] {
				count += (right - left)
				right--
			} else {
				left++
			}
		}
	}

	return count
}

// @leet end

