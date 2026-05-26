package main

import "strings"

// @leet start
func halvesAreAlike(s string) bool {
	// have a dict of vowels
	// split the string into two halves
	// sum up all the vowels in each
	// compare the sum
	vowels := map[byte]struct{}{
		'a': {}, 'e': {}, 'i': {}, 'o': {}, 'u': {},
	}

	counter := func(str string) int {
		var count int

		for _, char := range str {
			if _, ok := vowels[byte(char)]; ok {
				count++
			}
		}

		return count
	}

	n := len(s) / 2
	return counter(strings.ToLower(s[:n])) ==
		counter(strings.ToLower(s[n:]))
}

// @leet end

