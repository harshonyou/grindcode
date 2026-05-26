package main

// @leet start
func sumDigitsSquared(num int) int {
	var sum int

	for num > 0 {
		digit := num % 10
		num /= 10
		sum += digit * digit
	}

	return sum
}

func isHappy(n int) bool {
	// use the same logic as finding cycle in ll
	// have a slow ptr and fast ptr
	// if slow and fast ptr meets that means there must be cycle
	slow, fast := n, sumDigitsSquared(n)

	for fast != 1 && slow != fast {
		slow = sumDigitsSquared(slow)
		fast = sumDigitsSquared(sumDigitsSquared(fast))
	}

	return fast == 1
}

// @leet end

