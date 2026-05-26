package main

import "slices"

// @leet start
func sortedSquares(nums []int) []int {
	// have two ptrs -> left and right
	// iter nums from both dir
	// append the biggest num-squared to the result
	// reverse the result to get in-order
	leftPtr, rightPtr := 0, len(nums)-1
	result := make([]int, 0, len(nums))

	for leftPtr <= rightPtr {
		leftVal, rightVal := nums[leftPtr], nums[rightPtr]
		leftSqr, rightSqr := leftVal*leftVal, rightVal*rightVal

		if leftSqr > rightSqr {
			result = append(result, leftSqr)
			leftPtr++
		} else {
			result = append(result, rightSqr)
			rightPtr--
		}
	}

	slices.Reverse(result)
	return result
}

// @leet end

