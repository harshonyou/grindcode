package main

// @leet start
func backspaceCompare(s string, t string) bool {
	// iter from the end
	// if encounter '#', count them and keep skipping until count is 0
	// otherwise, check equality
	// return false if not equal, or one of them is out of bound
	n, m := len(s)-1, len(t)-1

	skipHash := func(idx int, str string) int {
		count := 0

	outer:
		for idx >= 0 {
			switch {
			case str[idx] == '#':
				count++
			case count > 0:
				count--
			default:
				break outer
			}

			idx--
		}

		return idx
	}

	for n >= 0 || m >= 0 {
		n = skipHash(n, s)
		m = skipHash(m, t)

		if n >= 0 && m >= 0 {
			if s[n] != t[m] {
				return false
			}
		} else if (n >= 0) != (m >= 0) {
			return false
		}

		n, m = n-1, m-1
	}

	return true
}

// @leet end
