package main

import "fmt"

// @leet start
func sumDigits(num int) int {
	var sum int

	for num > 0 {
		digit := num % 10
		num /= 10
		sum += digit
	}

	return sum
}

func getLucky(s string, k int) int {
	// sum the digits as such:
	// 123 % 10 = 3
	// 123 / 10 = 12
	// convert a char to int
	// hack: keep track of a global sum, to skip
	// storing an intermediate value
	var sum int

	for _, c := range s {
		sum += sumDigits(int(c) - 'a' + 1)
	}

	idx := 1
	for idx < k {
		sum = sumDigits(sum)
		idx++
	}

	return sum
}

// @leet end

