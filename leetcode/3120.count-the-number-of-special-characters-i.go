package main

// @leet start
func numberOfSpecialChars(word string) int {
	tracker := [26]uint8{}

	for _, c := range word {
		if c >= 'a' && c <= 'z' {
			tracker[c-'a'] |= 0b01
		} else {
			tracker[c-'A'] |= 0b10
		}
	}

	var count int
	for _, t := range tracker {
		if t == 0b11 {
			count++
		}
	}

	return count
}

// @leet end
