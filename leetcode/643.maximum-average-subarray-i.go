package main

// @leet start
func findMaxAverage(nums []int, k int) float64 {
	// find average of first k elements
	// iter from k to end of nums
	// on each iter remove (idx-k) from the average
	// and add (idx) to the average
	// if the running average is more than ever recorded then
	// consider it as potential
	var runningSum int
	var idx int

	for idx < k {
		runningSum += nums[idx]
		idx++
	}

	potential := runningSum

	for idx < len(nums) {
		runningSum -= nums[idx-k]
		runningSum += nums[idx]

		if runningSum > potential {
			potential = runningSum
		}
		idx++
	}

	return float64(potential) / float64(k)
}

// @leet end

