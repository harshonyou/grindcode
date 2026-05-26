package main

// @leet start
func findDuplicates(nums []int) []int {
	// have a bucket and count frequency
	// if any bucket elem has more than 1 count
	// return those numbers
	bucket := make([]int, len(nums))
	var res []int

	for _, num := range nums {
		bucket[num-1]++
	}

	for idx, count := range bucket {
		if count > 1 {
			res = append(res, idx+1)
		}
	}

	return res
}

// @leet end

