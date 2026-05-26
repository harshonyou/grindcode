package main

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

func countEven(num int) int {
	// need to split the digits
	// 123 % 10 = 3
	// 123 / 10 = 12
	// need to sum  up the digits (11 = 1 + 1 = 2)
	// need to find out even (2 % 2 = 0)
	var count int
	idx := 2

	for idx <= num {
		if sumDigits(idx)%2 == 0 {
			count++
		}

		idx++
	}

	return count
}

// @leet end

