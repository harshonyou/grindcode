package main

import (
	"math"
)

// @leet start
func sortedSquares(nums []int) []int {
	// iter nums to find idx where left is -ve and idx is +ve
	// -ve idx goes from right to left
	// +ve idx goes from left to right
	// append to ans arr the square of the smallest of those
	var (
		result   []int
		leftPtr  int
		rightPtr int
	)

	idx := len(nums) - 1
	if nums[idx] < 0 {
		idx = len(nums)
	} else if nums[0] >= 0 {
		idx = 0
	} else {
		for idx > 0 {
			if nums[idx-1] < 0 && nums[idx] >= 0 {
				break
			}

			idx--
		}
	}

	leftPtr, rightPtr = idx-1, idx

	for leftPtr >= 0 && rightPtr < len(nums) {
		leftVal := float64(nums[leftPtr])
		rightVal := float64(nums[rightPtr])

		if math.Abs(leftVal) < math.Abs(rightVal) {
			result = append(result, int(math.Pow(leftVal, 2)))
			leftPtr--
		} else {
			result = append(result, int(math.Pow(rightVal, 2)))
			rightPtr++
		}
	}

	// there will be either leftPtr and rightPtr still holding some more values, unless the split was even
	for leftPtr >= 0 {
		leftVal := float64(nums[leftPtr])
		result = append(result, int(math.Pow(leftVal, 2)))
		leftPtr--
	}

	for rightPtr < len(nums) {
		rightVal := float64(nums[rightPtr])
		result = append(result, int(math.Pow(rightVal, 2)))
		rightPtr++
	}

	return result
}

// @leet end

