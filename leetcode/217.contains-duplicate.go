package main

// @leet start
func containsDuplicate(nums []int) bool {
	// track seen obj
	seen := make(map[int]struct{})

	// iter num in nums
	// if have seen num, return true
	// otherwise, we update the seen obj
	for _, num := range nums {
		if _, ok := seen[num]; ok {
			return true
		}

		seen[num] = struct{}{}
	}

	// return false -> no duplicates found
	return false
}

// @leet end
