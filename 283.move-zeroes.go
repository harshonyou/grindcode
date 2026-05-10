package main

// @leet start
func moveZeroes(nums []int) {
	// have an slow & fast idx to iter nums
	// utilize the fast idx to find a non-zero val
	// override the slow idx and move it forward
	slowPtr, fastPtr := 0, 0

	for fastPtr < len(nums) {
		if nums[fastPtr] != 0 {
			nums[slowPtr] = nums[fastPtr]
			slowPtr++
		}
		fastPtr++
	}

	// replace all the elem [slow-idx, len(nums)) with 0
	for slowPtr < len(nums) {
		nums[slowPtr] = 0
		slowPtr++
	}
}

// @leet end

