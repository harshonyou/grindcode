package main

// @leet start
func missingNumber(nums []int) int {
	// properties of xor
	// x ^ 0 = x -> identity
	// x ^ x = 0 -> self-inverse
	// commutative and associative

	// find xor of nums given  - 3.0.1
	// find xor of range given - 0.1.2.3
	var xorNums int
	var xorRange int

	for idx, num := range nums {
		xorNums ^= num
		xorRange ^= idx
	}

	xorRange ^= len(nums)

	// find resultant xor from those two xor's
	return xorNums ^ xorRange
}

// @leet end
