package main

// @leet start
func isSubsequence(s string, t string) bool {
	// have ptrs pointing to both str
	// advance ptr to s, if only there exists a char at ptr t
	// that is of the same value, char at ptr s
	// if the ptr at s is pointing to the end, we have subsequence
	ptrS, ptrT := 0, 0

	for ptrS < len(s) && ptrT < len(t) {
		if s[ptrS] == t[ptrT] {
			ptrS++
		}

		ptrT++
	}

	return ptrS == len(s)
}

// @leet end

