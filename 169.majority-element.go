package main

// @leet start
func majorityElement(nums []int) int {
	// track an elem with freq as potential majority
	var potential int
	var freq int

	// iter num in nums
	// if encounter same num, inc freq
	// otherwise, dec freq
	// if freq dropped below 0,
	// then consider the next elem as potential successor
	for _, num := range nums {
		if potential == num {
			freq++
		} else {
			freq--
		}

		if freq < 0 {
			potential = num
			freq = 0
		}
	}

	// return the potential majority, as absolute
	return potential
}

// @leet end
