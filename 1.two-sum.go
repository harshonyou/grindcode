package main

// @leet start
func twoSum(nums []int, target int) []int {
	// track seen obj that maps to idx
	seen := make(map[int]int)

	// iter num in nums
	// for num, desired would be target - num
	// if we have seen desired, then return index of desired, current
	// otherwise update the tracked obj with current num
	for idx, num := range nums {
		desired := target - num

		if pastIdx, ok := seen[desired]; ok {
			return []int{pastIdx, idx}
		}

		seen[num] = idx
	}

	// return nil, since its guaranteed a solution
	return nil
}

// @leet end
