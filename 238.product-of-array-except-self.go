package main

// @leet start
func productExceptSelf(nums []int) []int {
	// calculate leftProduct and rightProduct
	// leftProduct, i -> nums0 * nums1 * ... * nums(i-1)
	// rightProduct, i -> nums(i+1) * nums(i+2) * ... * nums(len-1)
	// val we need -> leftProduct[i] * rightProduct[i]
	idx := 1
	n := len(nums)

	leftProduct := make([]int, n)
	rightProduct := make([]int, n)

	leftProduct[0] = nums[0]
	rightProduct[n-1] = nums[n-1]

	for idx < n {
		left := idx
		right := n - idx - 1

		leftProduct[left] = leftProduct[left-1] * nums[left]
		rightProduct[right] = rightProduct[right+1] * nums[right]

		idx++
	}

	idx = 0
	result := make([]int, n)
	for idx < n {
		left, right := 1, 1

		if idx > 0 {
			left = leftProduct[idx-1]
		}
		if idx < n-1 {
			right = rightProduct[idx+1]
		}

		result[idx] = left * right
		idx++
	}

	return result
}

// @leet end

