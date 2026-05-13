package main

// @leet start
func productExceptSelf(nums []int) []int {
	// calculate leftProduct and rightProduct
	// leftProduct, i -> nums0 * nums1 * ... * nums(i-1)
	// rightProduct, i -> nums(i+1) * nums(i+2) * ... * nums(len-1)
	// val we need -> leftProduct[i] * rightProduct[i]
	n := len(nums)
	res := make([]int, n)

	res[0] = 1
	for i := 1; i < n; i++ {
		res[i] = res[i-1] * nums[i-1]
	}

	right := 1
	for i := n - 1; i >= 0; i-- {
		res[i] = res[i] * right
		right *= nums[i]
	}

	return res
}

// @leet end

