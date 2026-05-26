package main

// @leet start
func search(nums []int, target int) int {
	// have two ptrs: left and right
	// init them at the front and back of the arr
	// find the mid idx of those two, and compare with target
	// if the num is smaller then it exists on the right region
	// if the num is greater then it exists on the left region
	// else you found the target
	leftPtr, rightPtr := 0, len(nums)-1

	for leftPtr <= rightPtr {
		midPtr := leftPtr + (rightPtr-leftPtr)/2
		val := nums[midPtr]

		if val < target {
			leftPtr = midPtr + 1
		} else if val > target {
			rightPtr = midPtr - 1
		} else {
			return midPtr
		}
	}

	return -1
}

// @leet end
