package main

// @leet start
func nextGreatestLetter(letters []byte, target byte) byte {
	// [a, c, d] - b
	// left -> 0(a), right -> 2(d); mid -> c(1) (b < c)
	// left -> 0(a), right -> 0(a); mid -> a(0) (return mid + 1)
	// if left is greater than right, return left % len(letters) (0 % 3 = 0 -> a)
	leftPtr, rightPtr := 0, len(letters)-1

	for leftPtr <= rightPtr {
		midPtr := leftPtr + (rightPtr-leftPtr)/2

		if letters[midPtr] <= target {
			leftPtr = midPtr + 1
		} else {
			rightPtr = midPtr - 1
		}
	}

	return letters[leftPtr%len(letters)]
}

// @leet end
