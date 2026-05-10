package main

// @leet start
func findDisappearedNumbers(nums []int) []int {
	// loop through the idx
	// keep swapping until elem,
	// at the current idx is not at the right pos
	var idx int
	for idx < len(nums) {
		targetIdx := nums[idx] - 1

		if nums[idx] != nums[targetIdx] {
			nums[idx], nums[targetIdx] = nums[targetIdx], nums[idx]
		} else {
			idx++
		}
	}

	// go through the list and check the missmatched idx
	var results []int
	for idx, num := range nums {
		if num != idx+1 {
			results = append(results, idx+1)
		}
	}

	return results
}

// @leet end
