package main

import (
	"slices"
)

// @leet start
func separateDigits(nums []int) []int {
	// logic to separate digits
	// 123 % 10 = 3
	// 123 / 10 = 12
	// since we'll be getting digits in reverse order,
	// we can just build an array in reverse
	// will just have to iter items from right to left
	idx := len(nums) - 1
	var result []int

	for idx >= 0 {
		num := nums[idx]

		for num > 0 {
			digit := num % 10
			num = num / 10
			result = append(result, digit)
		}

		idx--
	}

	slices.Reverse(result)
	return result
}

// @leet end

