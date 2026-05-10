package main

// @leet start
func isPalindrome(x int) bool {
	// reverse the number and check if the given is same
	// 1337 / 10 = 1337
	// 1337 % 10 = 7
	// 1337 * 10 = 13370
	var y int
	t := x

	for t > 0 {
		y *= 10
		digit := t % 10
		y += digit
		t /= 10
	}

	return x == y
}

// @leet end

