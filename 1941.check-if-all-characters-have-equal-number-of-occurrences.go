package main

// @leet start
func areOccurrencesEqual(s string) bool {
	// make a bucket of 26 elems to store the freq
	// at the end check if all the buckets are of same elem
	bucket := make([]int, 26)

	for _, c := range s {
		bucket[c-'a']++
	}

	count := bucket[s[0]-'a']

	for idx := 0; idx < 26; idx++ {
		if bucket[idx] != count && bucket[idx] != 0 {
			return false
		}
	}

	return true
}

// @leet end

