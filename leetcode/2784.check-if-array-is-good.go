package main

// @leet start
func isGood(nums []int) bool {
	// make bucket for size n
	// make sure all the bucket is of size 1
	// except for last one, i.e. 2
	n := len(nums) - 1
	buckets := make([]int, n)

	for _, num := range nums {
		if num > n {
			return false
		}
		buckets[num-1]++
	}

	if buckets[n-1] != 2 {
		return false
	}

	for _, num := range buckets[:n-1] {
		if num != 1 {
			return false
		}
	}

	return true
}

// @leet end

